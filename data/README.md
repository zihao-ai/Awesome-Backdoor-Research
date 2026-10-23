# Catalog data

The catalog JSON files are the source of the public README. Use UTF-8, two-space indentation, and a final newline. The catalog schemas reject JSON comments, duplicate keys, unknown fields, and trailing commas. All editorial strings are plain text, not Markdown or HTML.

## Taxonomy

[taxonomy.json](taxonomy.json) contains `version: 1` and an ordered `areas` array. Each area has `id`, `name`, `emoji`, `description`, and a nonempty `topics` array. Each topic has `id` and `name`.

IDs are lowercase letters/digits separated by hyphens. They remain stable when display names change. Area ID `computer-vision` becomes anchor `#area-computer-vision`; topic ID `image-classification` becomes `#topic-image-classification`. Reference topic IDs without the `topic-` prefix in paper records. The schema is [taxonomy.schema.json](../schemas/taxonomy.schema.json).

Area and topic array order is display order. Keep Surveys first. The 12 areas and 39 subcategories are all rendered even when empty. Never add fake records to fill an empty category.

## Papers

Each `papers/YYYY.json` is an array of records. Create a year file only when it has entries. The year is the publication year displayed in the table, not the date the entry was added to this list.

An existing example from [papers/2021.json](papers/2021.json):

```json
{
  "id": "wanet-2021",
  "title": "WaNet - Imperceptible Warping-based Backdoor Attack",
  "year": 2021,
  "venue": "ICLR",
  "url": "https://openreview.net/forum?id=eEn8KTtJOx",
  "types": ["Attack"],
  "topics": ["image-classification"],
  "code": "https://github.com/VinAIResearch/Warping-based_Backdoor_Attack-release"
}
```

| Field | Required | Meaning |
| :--- | :---: | :--- |
| `id` | Yes | Stable unique slug; keep it when updating a publication version |
| `title` | Yes | Full paper title, one line |
| `year` | Yes | Integer publication year; must match the year filename |
| `venue` | Yes | Concise venue name, or `arXiv` for a preprint |
| `url` | Yes | Primary HTTP(S) paper URL |
| `types` | Yes | Nonempty unique array drawn from `Attack`, `Defense`, `Analysis`, `Application`, `Survey`, `Benchmark`, `Dataset` |
| `topics` | Yes | Nonempty unique array of existing leaf topic IDs |
| `code` | No | GitHub repository root URL; omit if unavailable |

The schema is [papers.schema.json](../schemas/papers.schema.json). All paper files are validated together. IDs and normalized titles/URLs must not duplicate another paper. arXiv abstract/PDF URLs and version suffixes are recognized as the same identity. This catches common duplicates, not all possible aliases between publishers and preprint servers; search the catalog before adding an entry.

A single record may list multiple topics and will appear in each corresponding table. Do not copy the record into another file or create a second ID. Surveys use `general-surveys` or `surveys-specific`, with type `Survey`. Survey records are collected only in the Surveys area.

## Resources

[resources.json](resources.json) contains exactly three arrays: `tutorials` (including courses), `workshops`, and `toolboxes`. Empty arrays are valid; no placeholder records are necessary.

Tutorial and workshop fields: `id`, `title`, `year`, `venue`, `url`, `description`, and optional `links`. Use `venue` for the hosting conference, institution, or platform. Toolbox fields: `id`, `title`, `url`, `description`, and optional `links`. A toolbox's primary URL is its GitHub repository root.

`links` contains objects with `label` and `url`, for example:

```json
{
  "label": "Docs",
  "url": "https://ain-soph.github.io/trojanzoo/"
}
```

Use extra links for slides, recordings, documentation, or the event's paper list. A workshop paper itself belongs in `papers/`. A benchmark or dataset does not become a fourth resource group: list its associated paper in the appropriate paper table. The schema is [resources.schema.json](../schemas/resources.schema.json).

## Curation evidence

The files in `curation/` are editorial ledgers, separate from rendered paper fields:

- `legacy-migration.json` accounts for every historical paper row as migrated, duplicate, or excluded. Preserve its original row number, source line in the historical Git snapshot, and title. Retain canonical paper IDs when editing records.
- `expansion-reviews.json` records each added paper's abstract source, review date, classification rationale, and arXiv version when applicable. Identify secondary mirrors explicitly rather than claiming primary-source access.
- `searches.json` records topic queries and retrieval limits for the initial expansion pass. A result count is not a count of accepted papers.
- `recent-expansion.json` records the subsequent 2025–2026 query, retrieval and review counts, excluded candidates, and alias decisions. Its `batch_id` joins the corresponding entries in `expansion-reviews.json`.

These ledgers do not duplicate paper abstracts or feed the README renderer. The offline curation tests check archive accounting, paper references, and batch coverage. See the dated [coverage report](../docs/curation.md) for interpretation and limitations. Add later editorial batches without rewriting the historical evidence.

The separate [resource curation notes](../docs/resource-curation.md) document official sources, edition dates, scope boundaries, and availability limitations for the tutorial, course, workshop, and toolbox expansion.

## URLs and rendering

URLs must be absolute HTTP(S) addresses without credentials or whitespace. Code/toolbox links must point to `github.com/owner/repository`, with optional trailing slash or `.git`. Put a documentation URL in resource `links`, not in a GitHub icon cell. A missing paper implementation renders as `—`.

The renderer handles text escaping, Markdown links, and icon markup. Do not put icons, table delimiters, HTML, or formatting escapes into data fields. Record order in a year file does not control display order; rendering sorts by descending year, then venue, title, and ID.

Run `python scripts/validate.py` and `python scripts/build.py` from the repository root after editing. Validation is offline and does not check whether a paper's title, year, venue, or claimed contribution is factually correct.
