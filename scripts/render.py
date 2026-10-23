"""Deterministic GitHub-compatible Markdown for a validated catalog."""
from __future__ import annotations

from html import escape
import re
from urllib.parse import quote

from catalog import validate_template

PAPER_HEADER = "| Year / Venue | Paper | Type | Code |\n| :--- | :--- | :--- | :---: |"


def markdown_text(value: str) -> str:
    """Keep plain editorial text literal in Markdown links and table cells."""
    value = escape(value, quote=False)
    value = re.sub(r"([\\`*_{}\[\]()#+\-.!~])", r"\\\1", value)
    return value.replace("|", "&#124;")


def markdown_url(value: str) -> str:
    return quote(value, safe="/:?&=%+,;@#~!$'-._")


def link(label: str, url: str) -> str:
    return f"[{markdown_text(label)}]({markdown_url(url)})"


def github_icon(url: str) -> str:
    return (
        f'<a href="{escape(markdown_url(url), quote=True)}" title="Code repository">'
        '<picture><source media="(prefers-color-scheme: dark)" srcset="assets/github-mark-light.svg">'
        '<img src="assets/github-mark.svg" width="18" height="18" alt="GitHub">'
        '</picture></a>'
    )


def _navigation(areas: list[dict], papers: list[dict]) -> str:
    paper_ids_by_topic: dict[str, set[str]] = {}
    for paper in papers:
        for topic in paper['topics']:
            paper_ids_by_topic.setdefault(topic, set()).add(paper['id'])

    def cell(area: dict, attribute: str) -> str:
        area_papers: set[str] = set()
        topic_links = []
        for topic in area['topics']:
            topic_papers = paper_ids_by_topic.get(topic['id'], set())
            area_papers.update(topic_papers)
            topic_links.append(
                f'<a href="#topic-{topic["id"]}">{escape(topic["name"])} ({len(topic_papers)})</a>'
            )
        return (
            f'    <td {attribute} valign="top"><a href="#area-{area["id"]}"><strong>'
            f'{escape(area["emoji"])} {escape(area["name"])} ({len(area_papers)})</strong></a><br>\n'
            + '<br>\n'.join(topic_links) + '</td>'
        )

    lines = ["<table>", "  <tr>", cell(areas[0], 'colspan="2"'), "  </tr>"]
    for index in range(1, len(areas), 2):
        pair = areas[index:index + 2]
        lines.append("  <tr>")
        for area in pair:
            lines.append(cell(area, 'width="50%"' if len(pair) == 2 else 'colspan="2"'))
        lines.append("  </tr>")
    lines.append("</table>")
    return "\n".join(lines)


def _record_order(record: dict) -> tuple:
    return (-record.get("year", 0), record.get("venue", "").casefold(), record["title"].casefold(), record["id"])


def _papers(catalog: dict) -> str:
    records_by_topic: dict[str, list[dict]] = {}
    for record in sorted(catalog["papers"], key=_record_order):
        for topic in record["topics"]:
            records_by_topic.setdefault(topic, []).append(record)
    blocks = []
    for area in catalog["taxonomy"]["areas"]:
        blocks.extend([f'<a id="area-{area["id"]}"></a>', f'### {markdown_text(area["emoji"])} {markdown_text(area["name"])}'])
        for topic in area["topics"]:
            blocks.extend([f'<a id="topic-{topic["id"]}"></a>', f'#### {markdown_text(topic["name"])}'])
            rows = [PAPER_HEADER]
            for record in records_by_topic.get(topic["id"], []):
                year_venue = f'{record["year"]} · {markdown_text(record["venue"])}'
                types = " · ".join(f"`{value}`" for value in record["types"])
                code = github_icon(record["code"]) if record.get("code") else "—"
                rows.append(f'| {year_venue} | {link(record["title"], record["url"])} | {types} | {code} |')
            if len(rows) == 1:
                title = "Paper title (placeholder)"
                types = "—"
                if area["id"] == "surveys":
                    types = "`Survey`"
                    title = "General backdoor survey title (placeholder)" if topic["id"] == "general-surveys" else "Survey of a specific research direction (placeholder)"
                rows.append(f'| — | *{title}* | {types} | — |')
            blocks.append("\n".join(rows))
        blocks.append('<p align="right"><a href="#papers">↑ Research areas</a></p>')
    return "\n\n".join(blocks)


def _resource_list(records: list[dict]) -> str:
    if not records:
        return "*No resources listed yet.*"
    blocks = []
    for record in sorted(records, key=_record_order):
        text = f'- **{link(record["title"], record["url"])}** · {markdown_text(record["venue"])} {record["year"]}'
        if record.get("links"):
            text += "<br>\n  " + " · ".join(link(item["label"], item["url"]) for item in record["links"])
        blocks.append(text)
    return "\n\n".join(blocks)


def _toolboxes(records: list[dict]) -> str:
    rows = ["| Toolbox | Focus | Links |", "| :--- | :--- | :--- |"]
    for record in sorted(records, key=_record_order):
        links = [github_icon(record["url"])]
        links.extend(link(item["label"], item["url"]) for item in record.get("links", []))
        rows.append(f'| **{markdown_text(record["title"])}** | {markdown_text(record["description"])} | {" · ".join(links)} |')
    if not records:
        rows.append("| *Toolbox name (placeholder)* | — | — |")
    return "\n".join(rows)


def _catalog_stats(catalog: dict) -> str:
    areas = catalog['taxonomy']['areas']
    counts = ' · '.join(
        f'{count} {label}'
        for count, label in (
            (len(catalog['papers']), 'Papers'),
            (len(areas), 'Categories'),
            (sum(len(area['topics']) for area in areas), 'Subcategories'),
        )
    )
    return f'**{counts}**'


def render_readme(catalog: dict, template: str) -> str:
    """Render validated sources; no filesystem writes or network requests."""
    validate_template(template)
    generated = {
        "CATALOG_STATS": _catalog_stats(catalog),
        "AREA_NAVIGATION": _navigation(catalog["taxonomy"]["areas"], catalog["papers"]),
        "PAPERS": _papers(catalog),
        "TUTORIALS": _resource_list(catalog["resources"]["tutorials"]),
        "WORKSHOPS": _resource_list(catalog["resources"]["workshops"]),
        "TOOLBOXES": _toolboxes(catalog["resources"]["toolboxes"]),
    }
    # A single substitution prevents editorial content from introducing new slots.
    rendered = re.sub(r"\{\{(.*?)\}\}", lambda match: generated[match.group(1)], template)
    return rendered.rstrip() + "\n"
