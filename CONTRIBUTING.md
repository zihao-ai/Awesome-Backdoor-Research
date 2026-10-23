# Contributing

Help researchers find relevant backdoor papers, implementations, and learning resources. Small, focused contributions are welcome. The catalog combines migrated historical entries with newer abstract-reviewed papers and curated learning resources.

## Choose the right place

| Contribution | Edit |
| :--- | :--- |
| Paper, survey, benchmark paper, or dataset paper | `data/papers/YYYY.json` |
| Tutorial or course | `tutorials` in `data/resources.json` |
| Workshop or workshop series edition | `workshops` in `data/resources.json` |
| Reusable toolbox/framework | `toolboxes` in `data/resources.json` |
| New category or subcategory | `data/taxonomy.json` and the classification guidance |
| Introduction or reader-facing instructions | `templates/README.md` |
| Maintenance instructions | The relevant document in `docs/` |

Read the [taxonomy guide](docs/taxonomy.md) before classifying an entry and the [data guide](data/README.md) for fields and examples. The published README is generated: edit its sources and rebuild it.

## Propose an entry without running code

Open a paper or resource issue using the repository's issue templates. Include a primary URL, the intended subcategory, and a short explanation of relevance. Missing implementation code is fine; do not guess a repository URL. For corrections, identify the existing entry and provide supporting information.

An issue is a proposal, not an automatic addition. Paper validity and relevance require editorial judgment; passing the tooling only establishes that a record is structurally consistent.

## Edit and build locally

Use Python 3.11 or newer. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

1. Edit or create the appropriate JSON file. A year file is a JSON array; do not add comments or trailing commas.
2. Give each record a stable lowercase hyphenated ID. Reuse an existing paper record when adding another subcategory.
3. Use canonical paper links and plain-text titles. Omit optional `code` when no repository is known.
4. Run the following commands, then include both the source changes and generated README in the same pull request.

```bash
python scripts/validate.py
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

For a visual check:

```bash
python scripts/preview.py
```

Open [the local preview](http://127.0.0.1:8766/). Refresh it after editing the sources. Stop it with Ctrl+C. GitHub may render Markdown slightly differently.

## Selection and presentation

- Include work that directly studies backdoor behavior, attacks, defenses, analysis, or evaluation in the listed research settings. Generic adversarial attacks, prompt injection, or data poisoning do not automatically qualify as backdoor research.
- Prefer the publisher, conference, OpenReview, DOI, or arXiv landing page over a third-party summary. Preserve the paper's title and venue as published.
- Keep one record for the same work across preprint and proceedings versions. Update that record when publication information changes; move it to the corresponding year file if needed.
- Assign one or more paper types and the most relevant leaf topic IDs. Do not tag every setting mentioned in the introduction.
- Put surveys in Surveys. Put benchmark/dataset papers in their research subcategories with the corresponding paper types.
- Add a toolbox separately only when it is a reusable resource. A single paper's code usually belongs in that paper's `code` field.
- For tutorials, courses, and workshops, use the edition or teaching year stated by the organizer. Identify broader courses or workshops explicitly and confirm backdoor coverage in the syllabus, scope, or program. Put undated software documentation in the toolbox's extra links rather than inventing an event year.
- Describe resources factually in one sentence. Avoid promotional language, rankings, and unsupported claims about maintenance or completeness.
- Do not store PDFs, datasets, model weights, credentials, or other large artifacts in this catalog. Link to their authoritative public locations.

## Pull requests

Describe the change and the reason for its classification. Check for existing IDs, titles, and URLs first. Include validation/build results and disclose any links you could not confirm. Keep unrelated taxonomy changes and bulk migrations in separate pull requests.

Normal CI performs offline validation, tests, and a generation check. Live link auditing is a separate, optional command; see the [maintenance guide](docs/maintenance.md). The previous catalog remains available in Git history; preserve the historical accounting in the curation ledgers.

Contributions to repository files follow the existing [GPL-3.0 license](LICENSE). Linked papers, code, and resources retain their own licenses; listing a URL does not relicense its contents.
