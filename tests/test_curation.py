"""Check that the published curation evidence remains reconcilable with the catalog."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from catalog import is_http_url, load_catalog


class CurationEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog(ROOT)
        cls.papers = {p["id"]: p for p in cls.catalog["papers"]}
        cls.legacy = json.loads((ROOT / "data/curation/legacy-migration.json").read_text())
        cls.reviews = json.loads((ROOT / "data/curation/expansion-reviews.json").read_text())

    def test_original_rows_keep_complete_unique_source_line_references(self):
        self.assertEqual([row["legacy_row"] for row in self.legacy], list(range(1, 227)))
        lines = [row["archive_line"] for row in self.legacy]
        self.assertEqual(len(lines), len(set(lines)))
        for row in self.legacy:
            with self.subTest(row=row["legacy_row"]):
                self.assertGreater(row["archive_line"], 0)
                self.assertTrue(row["legacy_title"].strip())
                self.assertIn(row["status"], {"migrated", "duplicate", "excluded"})

    def test_duplicates_point_to_migrated_records_and_exclusions_have_reasons(self):
        migrated = {row["legacy_row"]: row["paper_id"] for row in self.legacy
                    if row["status"] == "migrated"}
        self.assertEqual(len(set(migrated.values())), len(migrated))
        for row in self.legacy:
            with self.subTest(row=row["legacy_row"]):
                if row["status"] == "excluded":
                    self.assertTrue(row["reason"].strip())
                    self.assertNotIn("paper_id", row)
                else:
                    self.assertIn(row["paper_id"], self.papers)
                    if row["status"] == "duplicate":
                        self.assertEqual(row["paper_id"], migrated[row["duplicate_of_row"]])
                    else:
                        self.assertTrue(is_http_url(row["abstract_source"]))

    def test_abstract_reviews_reference_distinct_new_papers_and_cover_all_topics(self):
        ids = [review["paper_id"] for review in self.reviews]
        self.assertEqual(len(ids), len(set(ids)))
        old_ids = {row["paper_id"] for row in self.legacy if "paper_id" in row}
        self.assertFalse(old_ids.intersection(ids))
        covered = set()
        for review in self.reviews:
            self.assertIn(review["paper_id"], self.papers)
            self.assertEqual(review["review_basis"], "abstract")
            self.assertTrue(is_http_url(review["abstract_source"]))
            self.assertTrue(review["classification_note"].strip())
            covered.update(self.papers[review["paper_id"]]["topics"])
        topics = {t["id"] for area in self.catalog["taxonomy"]["areas"] for t in area["topics"]}
        self.assertEqual(covered, topics)


if __name__ == "__main__":
    unittest.main()
