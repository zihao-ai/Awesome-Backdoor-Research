"""Behavior checks for the catalog's editorial data boundary."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from catalog import CatalogError, load_catalog


class CatalogFixture(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        shutil.copytree(REPO / "schemas", self.root / "schemas")
        (self.root / "data/papers").mkdir(parents=True)
        (self.root / "templates").mkdir()
        self.taxonomy = {
            "version": 1,
            "areas": [
                {"id": "surveys", "name": "Surveys", "emoji": "📖", "description": "Overview", "topics": [{"id": "general-surveys", "name": "General Surveys"}]},
                {"id": "vision", "name": "Vision", "emoji": "🖼️", "description": "Visual models", "topics": [{"id": "recognition", "name": "Recognition"}, {"id": "video", "name": "Video"}]},
            ],
        }
        self.paper = {"id": "example-2024", "title": "Example Paper", "year": 2024, "venue": "Conference", "url": "https://arxiv.org/abs/2401.12345", "types": ["Attack"], "topics": ["recognition"], "code": "https://github.com/research/example"}
        self.resources = {"tutorials": [], "workshops": [], "toolboxes": []}
        self.template = "# Example\n\n{{AREA_NAVIGATION}}\n\n{{PAPERS}}\n\n{{TUTORIALS}}\n\n{{WORKSHOPS}}\n\n{{TOOLBOXES}}\n"
        self.save()

    def write(self, path, data):
        (self.root / path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def save(self):
        self.write("data/taxonomy.json", self.taxonomy)
        self.write("data/papers/2024.json", [self.paper])
        self.write("data/resources.json", self.resources)
        (self.root / "templates/README.md").write_text(self.template, encoding="utf-8")


class CatalogTests(CatalogFixture):
    def test_empty_paper_collection_is_valid_without_fake_entries(self):
        self.write("data/papers/2024.json", [])
        catalog = load_catalog(self.root)
        self.assertEqual(catalog["papers"], [])

    def test_trailing_newlines_are_rejected_in_text_and_ids(self):
        for field in ("title", "venue", "id"):
            with self.subTest(field=field):
                bad = dict(self.paper)
                bad[field] += "\n"
                self.write("data/papers/2024.json", [bad])
                with self.assertRaises(CatalogError):
                    load_catalog(self.root)
        self.save()
        self.taxonomy["areas"][0]["description"] = "Overview\n"
        self.save()
        with self.assertRaises(CatalogError):
            load_catalog(self.root)
        self.taxonomy["areas"][0]["description"] = "Overview"
        self.resources["workshops"] = [{"id": "workshop", "title": "Workshop", "year": 2024,
            "venue": "Conference", "url": "https://example.org/workshop", "description": "Intro\n"}]
        self.save()
        with self.assertRaises(CatalogError):
            load_catalog(self.root)

    def test_multiple_known_topics_are_allowed_for_one_record(self):
        self.paper["topics"] = ["recognition", "video"]
        self.save()
        self.assertEqual(len(load_catalog(self.root)["papers"]), 1)

    def test_unknown_or_area_reference_is_rejected(self):
        for topic in ("missing", "vision"):
            with self.subTest(topic=topic):
                self.paper["topics"] = [topic]
                self.save()
                with self.assertRaisesRegex(CatalogError, "unknown topic"):
                    load_catalog(self.root)

    def test_duplicate_paper_ids_are_rejected_across_year_files(self):
        duplicate = dict(self.paper, year=2023, title="Different title", url="https://example.org/different")
        self.write("data/papers/2023.json", [duplicate])
        with self.assertRaisesRegex(CatalogError, "duplicate ID"):
            load_catalog(self.root)

    def test_duplicate_titles_ignore_case_whitespace_and_punctuation(self):
        duplicate = dict(self.paper, id="another-2024", title="EXAMPLE   Paper!", url="https://example.org/different")
        self.write("data/papers/2024.json", [self.paper, duplicate])
        with self.assertRaisesRegex(CatalogError, "duplicate paper title"):
            load_catalog(self.root)

    def test_arxiv_pdf_versions_and_abs_identify_same_paper(self):
        duplicate = dict(self.paper, id="another-2024", title="Different title", url="http://arxiv.org/pdf/2401.12345v3.pdf")
        self.write("data/papers/2024.json", [self.paper, duplicate])
        with self.assertRaisesRegex(CatalogError, "duplicate paper URL"):
            load_catalog(self.root)

    def test_year_mismatch_is_actionable(self):
        self.paper["year"] = 2025
        self.save()
        with self.assertRaisesRegex(CatalogError, "2024.json.*2025"):
            load_catalog(self.root)

    def test_schema_rejects_unknown_fields_empty_titles_and_repeated_topics(self):
        for field, value in (("typo", "value"), ("title", "  "), ("title", "One\nTwo"), ("topics", ["recognition", "recognition"])):
            with self.subTest(field=field, value=value):
                record = copy.deepcopy(self.paper)
                record[field] = value
                self.write("data/papers/2024.json", [record])
                with self.assertRaises(CatalogError):
                    load_catalog(self.root)

    def test_urls_reject_unsafe_or_malformed_destinations(self):
        for url in ("javascript:alert(1)", "file:///tmp/file", "https://", "https://user:secret@example.org/a", "https://example.org/a b", "https://example.org:bad/a"):
            with self.subTest(url=url):
                self.paper["url"] = url
                self.save()
                with self.assertRaises(CatalogError):
                    load_catalog(self.root)

    def test_code_links_must_target_github_repository_roots(self):
        for code in ("https://example.org/a/b", "https://github.com/owner", "https://github.com/owner/repo/issues/1", "https://github.com/owner/repo/tree/main", "https://github.com/owner/repo?tab=readme"):
            with self.subTest(code=code):
                self.paper["code"] = code
                self.save()
                with self.assertRaises(CatalogError):
                    load_catalog(self.root)
        self.paper["code"] = "https://github.com/owner/repo.git/"
        self.save()
        load_catalog(self.root)

    def test_surveys_must_use_survey_topics_and_survey_type(self):
        for types, topics in ((["Survey"], ["recognition"]), (["Attack"], ["general-surveys"]), (["Survey"], ["general-surveys", "recognition"])):
            with self.subTest(types=types, topics=topics):
                self.paper.update(types=types, topics=topics)
                self.save()
                with self.assertRaisesRegex(CatalogError, "Survey|survey"):
                    load_catalog(self.root)
        self.paper.update(types=["Survey"], topics=["general-surveys"])
        self.save()
        load_catalog(self.root)

    def test_duplicate_taxonomy_and_resource_ids_are_rejected(self):
        self.taxonomy["areas"][1]["topics"][1]["id"] = "recognition"
        self.save()
        with self.assertRaisesRegex(CatalogError, "duplicate ID"):
            load_catalog(self.root)
        self.taxonomy["areas"][1]["topics"][1]["id"] = "video"
        self.resources["toolboxes"] = [{"id": "example-2024", "title": "Toolbox", "url": "https://github.com/owner/repo", "description": "Framework"}]
        self.save()
        with self.assertRaisesRegex(CatalogError, "duplicate ID"):
            load_catalog(self.root)

    def test_duplicate_json_keys_are_not_silently_overwritten(self):
        (self.root / "data/resources.json").write_text('{"tutorials": [], "tutorials": [], "workshops": [], "toolboxes": []}', encoding="utf-8")
        with self.assertRaisesRegex(CatalogError, "resources.json.*duplicate JSON key"):
            load_catalog(self.root)

    def test_template_slots_must_be_known_and_exactly_once(self):
        for template in (self.template.replace("{{PAPERS}}", ""), self.template + "{{PAPERS}}", self.template + "{{OTHER}}"):
            with self.subTest(template=template):
                (self.root / "templates/README.md").write_text(template, encoding="utf-8")
                with self.assertRaisesRegex(CatalogError, "template|Template"):
                    load_catalog(self.root)

    def test_non_year_data_files_fail_instead_of_being_silently_skipped(self):
        self.write("data/papers/misc.json", [])
        with self.assertRaisesRegex(CatalogError, "YYYY.json"):
            load_catalog(self.root)


if __name__ == "__main__":
    unittest.main()
