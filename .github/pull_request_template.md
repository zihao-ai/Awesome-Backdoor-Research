## Change

Describe the entries, classification changes, or maintenance behavior introduced by this PR.

## Rationale

Explain category choices and cite primary sources for metadata corrections. Note any uncertain or unavailable implementation links.

## Checks

- [ ] Edited structured data/template rather than only generated README.
- [ ] Checked for duplicate records and preprint/proceedings versions.
- [ ] Used leaf topic IDs; placed surveys in Surveys and benchmark/dataset papers in their research areas.
- [ ] `python scripts/validate.py` passes.
- [ ] Ran `python scripts/build.py` and included the generated README.
- [ ] `python scripts/build.py --check` passes.
- [ ] `python -m unittest discover -s tests -v` passes.

For documentation-only changes, mark checks that do not apply and explain why. Live link audits are optional; disclose unresolved link issues if relevant.
