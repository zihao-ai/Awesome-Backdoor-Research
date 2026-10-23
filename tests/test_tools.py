"""Exercise maintenance tools against local fixtures, never live paper websites."""
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_links import audit_links, collect_urls, exit_status
from preview import export_preview, make_handler, render_page
from test_catalog import CatalogFixture


@contextmanager
def serving(handler):
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{server.server_port}'
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


class LinkEndpoint(BaseHTTPRequestHandler):
    requests = []

    def do_HEAD(self):
        self.respond()

    def do_GET(self):
        self.respond()

    def respond(self):
        self.requests.append((self.command, self.path))
        status = {'/missing': 404, '/gone': 410, '/blocked': 403,
                  '/limited': 429, '/server-error': 503}.get(self.path, 200)
        if self.path == '/get-only' and self.command == 'HEAD':
            status = 405
        if self.path == '/redirect':
            self.send_response(302)
            self.send_header('Location', '/ok')
        elif self.path == '/slow':
            time.sleep(0.15)
            self.send_response(200)
        else:
            self.send_response(status)
        self.end_headers()

    def log_message(self, *args):
        pass


class LinkTests(unittest.TestCase):
    def test_classifies_failures_without_calling_blocks_broken(self):
        with serving(LinkEndpoint) as base:
            paths = ['/ok', '/redirect', '/get-only', '/missing', '/gone',
                     '/blocked', '/limited', '/server-error']
            rows = audit_links([base + path for path in paths], timeout=1, workers=2)
        by_path = {row['url'].replace(base, ''): row for row in rows}
        self.assertEqual({path: row['status'] for path, row in by_path.items()}, {
            '/ok': 'ok', '/redirect': 'ok', '/get-only': 'ok',
            '/missing': 'broken', '/gone': 'broken', '/blocked': 'blocked',
            '/limited': 'blocked', '/server-error': 'unreachable'})
        self.assertEqual(by_path['/redirect']['final_url'], base + '/ok')
        self.assertIn(('GET', '/get-only'), LinkEndpoint.requests)
        self.assertEqual(exit_status(rows), 1)

    def test_malformed_http_response_does_not_abort_other_results(self):
        class BrokenEndpoint(LinkEndpoint):
            def respond(self):
                if self.path == '/malformed':
                    self.wfile.write(b'BROKEN RESPONSE\r\n\r\n')
                    self.close_connection = True
                else:
                    super().respond()
        with serving(BrokenEndpoint) as base:
            rows = audit_links([base + '/malformed', base + '/ok'], timeout=1, workers=2)
        self.assertEqual([row['status'] for row in rows], ['unreachable', 'ok'])
        self.assertIn('BROKEN RESPONSE', rows[0]['detail'])

    def test_timeout_is_uncertain_and_strict_mode_can_fail(self):
        with serving(LinkEndpoint) as base:
            rows = audit_links([base + '/slow'], timeout=0.03, workers=1)
        self.assertEqual(rows[0]['status'], 'unreachable')
        self.assertEqual(exit_status(rows), 0)
        self.assertEqual(exit_status(rows, strict=True), 2)

    def test_fragments_are_deduplicated_before_requests(self):
        LinkEndpoint.requests = []
        with serving(LinkEndpoint) as base:
            rows = audit_links([base + '/ok#one', base + '/ok#two', base + '/ok'], timeout=1)
        self.assertEqual(len(rows), 1)
        self.assertEqual(LinkEndpoint.requests, [('HEAD', '/ok')])

    def test_collects_paper_code_and_resource_links_without_archives(self):
        catalog = {'papers': [{'url': 'https://example.org/paper', 'code': 'https://github.com/a/b'}],
                   'resources': {'tutorials': [{'url': 'https://example.org/learn', 'links': [
                       {'label': 'Slides', 'url': 'https://example.org/slides'}]}],
                       'workshops': [], 'toolboxes': [{'url': 'https://github.com/a/b'}]}}
        self.assertEqual(collect_urls(catalog), ['https://example.org/learn',
            'https://example.org/paper', 'https://example.org/slides', 'https://github.com/a/b'])

    def test_invalid_request_options_fail_before_starting(self):
        for options in ({'timeout': 0}, {'workers': 0}, {'workers': 33}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                audit_links([], **options)


class PreviewTests(unittest.TestCase):
    def test_markdown_tables_and_explicit_anchors_render(self):
        result = render_page('<a id="topic-sample"></a>\n\n#### Sample\n\n'
                             '| Year | Code |\n| :--- | :---: |\n| 2024 | — |\n')
        self.assertIn('<table>', result)
        self.assertIn('<th', result)
        self.assertIn('id="topic-sample"', result)
        self.assertIn('href="/assets/preview.css"', result)
        self.assertIn('name="viewport"', result)

    def test_server_serves_docs_but_never_git_environment_or_traversal(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'docs').mkdir()
            (root / 'docs/guide.md').write_text('# Guide\n\n[Home](../README.md)\n')
            (root / '.git').mkdir()
            (root / '.git/config').write_text('SECRET')
            (root / '.env').write_text('SECRET')
            (root / 'docs/escape.md').symlink_to(root / '.env')
            with serving(make_handler(root)) as base:
                with urlopen(base + '/docs/guide.md') as response:
                    self.assertIn('<h1', response.read().decode())
                for path in ['/.git/config', '/.env', '/docs/../.env',
                             '/docs/%2e%2e/.env', '/docs/escape.md', '/scripts/build.py']:
                    with self.subTest(path=path), self.assertRaises(HTTPError) as caught:
                        urlopen(base + path)
                    self.assertEqual(caught.exception.code, 404)
                    caught.exception.close()


class ExportTests(CatalogFixture):
    def test_snapshot_keeps_doc_links_assets_and_public_data_resolvable(self):
        (self.root / 'docs').mkdir()
        (self.root / 'docs/guide.md').write_text('[Data](../data/taxonomy.json) [Home](../README.md)')
        (self.root / 'assets').mkdir()
        (self.root / 'assets/preview.css').write_text('body {color: black}')
        destination = self.root / '.preview'
        result = export_preview(self.root, destination)
        self.assertTrue(result.exists())
        guide = (destination / 'docs/guide.html').read_text()
        self.assertIn('href="../README.html"', guide)
        self.assertIn('href="../assets/preview.css"', guide)
        self.assertTrue((destination / 'data/taxonomy.json').exists())
        self.assertTrue((destination / 'schemas/papers.schema.json').exists())
        with serving(make_handler(self.root)) as base:
            with urlopen(base + '/data/taxonomy.json') as response:
                self.assertIn('surveys', response.read().decode())
            with urlopen(base + '/schemas/papers.schema.json') as response:
                self.assertIn('application/json', response.headers['Content-Type'])

    def test_export_rejects_source_directories_before_writing(self):
        for directory in (self.root, self.root / 'data', self.root / 'docs/export', self.root / 'assets'):
            with self.subTest(directory=directory), self.assertRaises(ValueError):
                export_preview(self.root, directory)


if __name__ == '__main__':
    unittest.main()
