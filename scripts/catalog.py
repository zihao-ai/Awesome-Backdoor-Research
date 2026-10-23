"""Load and validate catalog sources without making network requests."""
from __future__ import annotations

import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[1]
SLOTS = ("CATALOG_STATS", "AREA_NAVIGATION", "PAPERS", "TUTORIALS", "WORKSHOPS", "TOOLBOXES")
FORMATS = FormatChecker()


class CatalogError(ValueError):
    """An actionable data, schema, or template validation error."""


@FORMATS.checks("http-url")
def is_http_url(value: object) -> bool:
    if not isinstance(value, str) or re.search(r"[\s\x00-\x1f\x7f\\]", value):
        return False
    try:
        parsed = urlsplit(value)
        return bool(
            parsed.scheme.lower() in {"http", "https"}
            and parsed.hostname
            and parsed.username is None
            and parsed.password is None
            and parsed.port != 0
            and not re.search(r'[<>"{}|^`]', value)
        )
    except ValueError:
        return False


@FORMATS.checks("github-repository")
def is_github_repository(value: object) -> bool:
    if not is_http_url(value):
        return False
    parsed = urlsplit(value)
    return bool(
        parsed.hostname.lower() == "github.com"
        and parsed.port is None
        and not parsed.query
        and not parsed.fragment
        and re.fullmatch(r"/[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?/[A-Za-z0-9_.-]+/?", parsed.path)
        and parsed.path.rstrip("/").split("/")[-1] not in {".", "..", ".git"}
    )


def _unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise CatalogError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError, CatalogError) as exc:
        raise CatalogError(f"{path}: {exc}") from exc


def _validate_schema(data: object, name: str, path: Path, root: Path) -> None:
    schema_path = root / "schemas" / f"{name}.schema.json"
    schema = read_json(schema_path)
    try:
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FORMATS)
        errors = sorted(validator.iter_errors(data), key=lambda error: str(list(error.absolute_path)))
    except SchemaError as exc:
        raise CatalogError(f"{schema_path}: invalid JSON Schema: {exc.message}") from exc
    if errors:
        details = []
        for error in errors[:20]:
            location = "/" + "/".join(str(item) for item in error.absolute_path)
            details.append(f"{path}:{location}: {error.message}")
        raise CatalogError("\n".join(details))


def validate_template(template: str) -> None:
    tokens = re.findall(r"\{\{(.*?)\}\}", template, flags=re.DOTALL)
    unknown = sorted(set(tokens) - set(SLOTS))
    if unknown:
        raise CatalogError(f"README template contains unknown slots: {', '.join(unknown)}")
    for name in SLOTS:
        count = tokens.count(name)
        if count != 1:
            raise CatalogError(f"README template slot {{{{{name}}}}} must occur exactly once (found {count})")
    if "{{" in re.sub(r"\{\{.*?\}\}", "", template, flags=re.DOTALL):
        raise CatalogError("README template contains an unclosed slot")


def normalized_title(title: str) -> str:
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFKC", title).casefold())


def normalized_paper_url(url: str) -> str:
    """Recognize common identity variants; never infer a paper's accuracy."""
    parsed = urlsplit(url)
    hostname = parsed.hostname.lower()
    hostname = hostname.removeprefix("www.")
    path = parsed.path.rstrip("/")
    if hostname in {"arxiv.org", "export.arxiv.org"}:
        match = re.fullmatch(r"/(?:abs|pdf)/(.+?)(?:\.pdf)?", path)
        if match:
            identifier = re.sub(r"v\d+$", "", match.group(1))
            return f"arxiv:{identifier.lower()}"
    if hostname in {"doi.org", "dx.doi.org"}:
        return f"doi:{path.lstrip('/').casefold()}"
    query = urlencode(sorted((key, value) for key, value in parse_qsl(parsed.query, keep_blank_values=True) if not key.lower().startswith("utm_")))
    port = f":{parsed.port}" if parsed.port and parsed.port not in {80, 443} else ""
    return urlunsplit(("https", hostname + port, path, query, ""))


def load_catalog(root: Path = ROOT) -> dict:
    """Return validated taxonomy, flat paper records, and resource groups."""
    root = Path(root)
    taxonomy_path = root / "data/taxonomy.json"
    resources_path = root / "data/resources.json"
    taxonomy = read_json(taxonomy_path)
    resources = read_json(resources_path)
    _validate_schema(taxonomy, "taxonomy", taxonomy_path, root)
    _validate_schema(resources, "resources", resources_path, root)
    template_path = root / "templates/README.md"
    try:
        validate_template(template_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        raise CatalogError(f"{template_path}: {exc}") from exc

    ids: dict[str, str] = {}

    def claim_id(identifier: str, source: str) -> None:
        if identifier in ids:
            raise CatalogError(f"{source}: duplicate ID {identifier!r}; first used in {ids[identifier]}")
        ids[identifier] = source

    areas = taxonomy["areas"]
    if areas[0]["id"] != "surveys":
        raise CatalogError(f"{taxonomy_path}: Surveys (id 'surveys') must be the first area")
    known_topics: set[str] = set()
    survey_topics: set[str] = set()
    for area in areas:
        claim_id(area["id"], f"{taxonomy_path}: area")
        for topic in area["topics"]:
            claim_id(topic["id"], f"{taxonomy_path}: topic in {area['id']}")
            known_topics.add(topic["id"])
            if area["id"] == "surveys":
                survey_topics.add(topic["id"])

    papers = []
    titles: dict[str, str] = {}
    urls: dict[str, str] = {}
    directory = root / "data/papers"
    if not directory.is_dir():
        raise CatalogError(f"{directory}: missing paper data directory")
    for path in sorted(directory.glob("*.json")):
        if not re.fullmatch(r"\d{4}\.json", path.name):
            raise CatalogError(f"{path}: paper files must use the name YYYY.json")
        records = read_json(path)
        _validate_schema(records, "papers", path, root)
        for record in records:
            source = f"{path}: {record['id']}"
            claim_id(record["id"], source)
            if record["year"] != int(path.stem):
                raise CatalogError(f"{path}: {record['id']} has year {record['year']}; it must match filename year {path.stem}")
            unknown = set(record["topics"]) - known_topics
            if unknown:
                raise CatalogError(f"{source}: unknown topic references: {', '.join(sorted(unknown))}")
            if "Survey" in record["types"]:
                if not set(record["topics"]).issubset(survey_topics):
                    raise CatalogError(f"{source}: Survey papers must use only survey topics")
            elif set(record["topics"]) & survey_topics:
                raise CatalogError(f"{source}: survey topics require the Survey paper type")
            for identity, seen, label in ((normalized_title(record["title"]), titles, "title"), (normalized_paper_url(record["url"]), urls, "URL")):
                if identity in seen:
                    raise CatalogError(f"{source}: duplicate paper {label}; already used by {seen[identity]}")
                seen[identity] = record["id"]
            papers.append(record)
    for group, entries in resources.items():
        for entry in entries:
            claim_id(entry["id"], f"{resources_path}: {group}")
    return {"taxonomy": taxonomy, "papers": papers, "resources": resources}
