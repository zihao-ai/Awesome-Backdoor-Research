"""Renderer and CLI checks use real source fixtures and subprocesses."""
from __future__ import annotations

import subprocess
import sys
import unittest

import markdown

from test_catalog import CatalogFixture, REPO
from catalog import load_catalog
from render import render_readme


class RenderingTests(CatalogFixture):
    def render(self):
        self.save()
        return render_readme(load_catalog(self.root), self.template)

    def test_empty_leaf_tables_and_navigation_remain_visible(self):
        output = self.render()
        self.assertIn('colspan="2"', output)
        self.assertIn('id="topic-video"', output)
        self.assertIn('#### Video\n\n| Year / Venue | Paper | Type | Code |', output)
        self.assertIn('*Paper title (placeholder)*', output)
        self.assertEqual(output.count('| Year / Venue | Paper | Type | Code |'), 3)
        self.assertIn('colspan="2"', output.split('href="#area-vision"')[0].split('<tr>')[-1])

    def test_one_record_renders_in_each_of_its_topics(self):
        self.paper["topics"] = ["recognition", "video"]
        output = self.render()
        self.assertEqual(output.count('[Example Paper]'), 2)
        self.assertEqual(output.count('title="Code repository"'), 2)
        self.assertNotIn('Official implementation', output)

    def test_missing_code_renders_dash(self):
        del self.paper["code"]
        output = self.render()
        self.assertIn('| `Attack` | — |', output)

    def test_untrusted_text_and_url_punctuation_cannot_break_a_table(self):
        self.paper["title"] = '[A | B] <img src=x onerror="alert(1)"> *literal*'
        self.paper["venue"] = "A | B"
        self.paper["url"] = "https://example.org/paper_(test)?x=1&y=2"
        output = self.render()
        row = next(line for line in output.splitlines() if "example.org/paper" in line)
        self.assertEqual(row.count("|"), 5)
        self.assertIn('&#124;', row)
        self.assertIn('&lt;img', row)
        self.assertIn('\\[A', row)
        self.assertIn('%28test%29', row)
        self.assertNotIn('<img src=x', row)

    def test_plain_text_resource_descriptions_do_not_create_markdown_blocks(self):
        for description in ("+ bullet", "- bullet", "1. numbered", "# heading", "---"):
            with self.subTest(description=description):
                self.resources["tutorials"] = [{"id": "tutorial", "title": "Learn", "year": 2024,
                    "venue": "Course", "url": "https://example.org/learn", "description": description}]
                output = markdown.markdown(self.render(), extensions=["tables"])
                self.assertEqual(output.count('<li>'), 1)
                self.assertNotIn('<ol>', output)
                self.assertNotIn('<hr', output)
                self.assertNotIn('<h1>heading', output)
                self.assertIn(description, output)

    def test_order_is_stable_and_newer_papers_come_first(self):
        old = dict(self.paper, id="older-2023", title="Older", year=2023, url="https://example.org/older")
        self.write("data/papers/2023.json", [old])
        catalog = load_catalog(self.root)
        first = render_readme(catalog, self.template)
        catalog["papers"].reverse()
        second = render_readme(catalog, self.template)
        self.assertEqual(first, second)
        self.assertLess(first.index('[Example Paper]'), first.index('[Older]'))


class BuildCliTests(CatalogFixture):
    def build(self, *args):
        return subprocess.run([sys.executable, str(REPO / "scripts/build.py"), "--root", str(self.root), *args], capture_output=True, text=True)

    def test_check_is_read_only_and_reports_stale_then_fresh(self):
        readme = self.root / "README.md"
        readme.write_text("keep me\n", encoding="utf-8")
        stale = self.build("--check")
        self.assertNotEqual(stale.returncode, 0, stale.stdout + stale.stderr)
        self.assertEqual(readme.read_text(), "keep me\n")
        built = self.build()
        self.assertEqual(built.returncode, 0, built.stdout + built.stderr)
        before = readme.stat().st_mtime_ns
        fresh = self.build("--check")
        self.assertEqual(fresh.returncode, 0, fresh.stdout + fresh.stderr)
        self.assertEqual(readme.stat().st_mtime_ns, before)

    def test_invalid_data_does_not_overwrite_readme(self):
        self.paper["topics"] = ["unknown"]
        self.save()
        readme = self.root / "README.md"
        readme.write_text("keep me\n", encoding="utf-8")
        failed = self.build()
        self.assertNotEqual(failed.returncode, 0, failed.stdout + failed.stderr)
        self.assertIn("unknown topic", failed.stderr)
        self.assertEqual(readme.read_text(), "keep me\n")


if __name__ == "__main__":
    unittest.main()
