# Maintenance

See [architecture](architecture.md) for file responsibilities and [taxonomy](taxonomy.md) for classification decisions. Reader-facing content remains in English; changes to the repository's GitHub name or URL are independent of its display title.

## Environment and routine checks

Use Python 3.11 or newer. Install tooling in an isolated environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The two direct dependencies are `jsonschema` for record validation and `Markdown` for the optional preview. Runtime ranges are bounded by major version in `requirements.txt`; review changes before broadening them. The implementation uses the [jsonschema validation API](https://python-jsonschema.readthedocs.io/en/stable/validate/) and Python-Markdown's [table extension](https://python-markdown.github.io/extensions/tables/).

| Command | Effect |
| :--- | :--- |
| `python scripts/validate.py` | Validate schemas, references, duplicates, year placement, URLs, and template slots offline |
| `python scripts/build.py` | Validate, then atomically update `README.md` if needed |
| `python scripts/build.py --check` | Validate and fail if README is stale; never write it |
| `python -m unittest discover -s tests -v` | Test real loading/rendering/CLI behavior and local HTTP fixtures |
| `python scripts/preview.py` | Serve an approximation of GitHub rendering at `127.0.0.1:8766` |
| `python scripts/preview.py --output .preview` | Export a local HTML snapshot, including documentation and assets |
| `python scripts/check_links.py --list` | List current source URLs without contacting them |
| `python scripts/check_links.py` | Audit current source URLs and write `reports/links.json` |

Every script accepts `--root PATH`; its default is the checkout containing that script, regardless of the shell's working directory. Generated report/output paths are relative to that root unless absolute. Run `--help` for available flags.

## Editing and regeneration

Edit JSON records or `templates/README.md`, validate, build, and commit source plus generated README together. The template contains these five slots exactly once:

```text
{{AREA_NAVIGATION}}
{{PAPERS}}
{{TUTORIALS}}
{{WORKSHOPS}}
{{TOOLBOXES}}
```

Keep generated sections out of the template. Text escaping, icon markup, table headers, stable anchors, sorting, and empty-state rows are renderer responsibilities. Edit `scripts/render.py` to change that behavior and add a behavioral test for the change.

A successful build is deterministic and adds no timestamp. Invalid source data leaves the previous README untouched. CI checks freshness instead of silently rebuilding and committing on a contributor's behalf.

## Local preview

The preview builds the current source data in memory on each refresh, so no generated README update is required to inspect an edit. The server binds only to loopback. It serves the catalog and intended public documentation/assets; repository configuration, virtual environments, and arbitrary working files are not exposed.

Use `--port 8767` if another preview already uses 8766. `--output .preview` exports a snapshot rather than starting a server; open `.preview/index.html` locally. Re-export after changes. The CSS supports narrow windows and light/dark appearance. GitHub controls the actual repository rendering, including sanitization and styling.

## Optional live link audit

Normal catalog checks do not make paper-site requests. Explicitly run a link audit when ready:

```bash
python scripts/check_links.py --timeout 10 --workers 4
```

The checker deduplicates current paper, code, and resource URLs, ignores URL fragments, follows a bounded number of redirects, and falls back from HEAD to GET where HEAD may be unsupported or blocked. GET does not download the response body. The timeout applies to individual socket operations; a redirect chain can take longer than one timeout. There are no automatic retry loops.

| Result | Interpretation |
| :--- | :--- |
| `ok` | The server returned a successful response; content was not verified |
| `broken` | The endpoint returned HTTP 404 or 410; inspect the source before changing it |
| `blocked` | Authentication/access protection or rate limiting (401, 403, 429) |
| `unreachable` | Timeout, DNS/TLS/network failure, server error, or another inconclusive response |

Exit code 1 means at least one broken URL. Exit code 0 means no confirmed broken URLs, not that every URL was reachable. `--strict` additionally returns 2 when blocked/unreachable results remain. Configuration or validation failures return 2. `--list` makes no network requests.

The report never edits records. Check canonical publisher/project locations manually before replacing links, and never delete a paper merely because a URL failed. The historical archive is excluded from live audits.

## GitHub automation

- **Validate catalog** runs on pull requests, pushes to `main`, and manual dispatch. It installs dependencies, validates, runs tests on Python 3.11 and 3.14, checks generated freshness, and checks whitespace. Catalog checks themselves require no external network.
- **Audit catalog links** runs only on manual dispatch. It writes the JSON report and includes it in the Actions job summary for inspection. It is not a required pull-request check.
- Both workflows use `contents: read`; neither commits data, opens issues, or publishes a site. Checkout and Python setup follow their official [checkout](https://github.com/actions/checkout) and [setup-python](https://github.com/actions/setup-python) usage guidance.

These workflow files take effect after they are pushed to GitHub. Local test success does not mean a hosted workflow has run.

## Migrating the historical collection

The October 2026 migration accounts for all 226 historical paper rows: 212 independent papers migrated, seven duplicate rows merged, and seven scope exclusions documented. The catalog also contains four previously reviewed examples outside that collection, 90 initial abstract-reviewed additions, and 146 subsequent additions focused on 2025–2026, for 452 independent papers. See [curation and coverage](curation.md) and the ledgers in `data/curation/`. [The original collection](https://github.com/zihao-ai/Awesome-Backdoor-Research/blob/4be174fceda6034a8b7856a56a848e5b10adc097/README.md) is available in Git history.

For further expansion, work through one leaf topic at a time: search for candidates, read their abstracts, identify the actual victim task and contribution, resolve preprint/proceedings aliases, and add records with known implementation links. Record the abstract source and rationale in the expansion review ledger. Do not download PDFs or infer classifications solely from search terms. Validate/build after each batch.

The retired parser has been removed. Use the current scripts under `scripts/`; historical source is available in Git history.

## Extending the repository

Add fields through the relevant schema, loader/renderer where needed, data guide, and tests together. New output views should consume the existing records. A separate website, search index, release package, or per-topic page set can be added when its benefit justifies the maintenance cost; none is required to use this catalog.

The dated curation report describes the limits of the October 2026 pass. Keep later batch claims similarly bounded: filling every category does not establish bibliographic completeness.
