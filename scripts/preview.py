#!/usr/bin/env python3
"""Preview the catalog locally, or export an HTML snapshot with --output DIRECTORY."""
from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import html
import mimetypes
import os
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote, urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = {'README.md', 'CONTRIBUTING.md', 'LICENSE'}


def render_page(source: str, stylesheet: str = '/assets/preview.css') -> str:
    body = markdown.markdown(source, extensions=['tables', 'fenced_code', 'toc', 'sane_lists'])

    def local_html(match: re.Match) -> str:
        url = match[1]
        if urlsplit(url).scheme or url.startswith('//'):
            return match[0]
        return 'href="' + re.sub(r'\.md(?=[#?]|$)', '.html', url) + '"'

    body = re.sub(r'href="([^"]+)"', local_html, body)
    return ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>Awesome Backdoor Research</title>'
            f'<link rel="stylesheet" href="{html.escape(stylesheet, quote=True)}">'
            f'</head><body><article class="markdown-body">{body}</article></body></html>\n')


def catalog_markdown(root: Path) -> str:
    from catalog import load_catalog
    from render import render_readme
    return render_readme(load_catalog(root), (root / 'templates/README.md').read_text(encoding='utf-8'))


def allowed_file(root: Path, relative: str) -> Path | None:
    parts = Path(relative).parts
    if not parts or any(part in ('.', '..') or part.startswith('.') for part in parts):
        return None
    candidate = root / relative
    if candidate.resolve() != candidate.absolute() or not candidate.is_file():
        return None
    if relative in ROOT_FILES or relative == 'data/README.md':
        return candidate
    if relative in ('data/taxonomy.json', 'data/resources.json'):
        return candidate
    if re.fullmatch(r'data/papers/[0-9]{4}\.json', relative):
        return candidate
    if re.fullmatch(r'schemas/[a-z-]+\.schema\.json', relative):
        return candidate
    if parts[0] == 'docs' and candidate.suffix == '.md':
        return candidate
    if parts[0] == 'assets' and candidate.suffix in ('.svg', '.css', '.txt'):
        return candidate
    return None


def make_handler(root: Path) -> type[BaseHTTPRequestHandler]:
    root = root.resolve()

    class PreviewHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.serve(send_body=True)

        def do_HEAD(self):
            self.serve(send_body=False)

        def serve(self, send_body: bool):
            relative = unquote(urlsplit(self.path).path).lstrip('/')
            if relative in ('', 'index.html', 'README.html', 'README.md'):
                try:
                    body = render_page(catalog_markdown(root)).encode('utf-8')
                except (ValueError, OSError) as error:
                    self.send_error(500, f'Catalog build failed: {error}')
                    return
                content_type = 'text/html; charset=utf-8'
            else:
                if relative.endswith('.html'):
                    relative = relative[:-5] + '.md'
                path = allowed_file(root, relative)
                if path is None:
                    self.send_error(404)
                    return
                if path.suffix == '.md':
                    body = render_page(path.read_text(encoding='utf-8')).encode('utf-8')
                    content_type = 'text/html; charset=utf-8'
                else:
                    body = path.read_bytes()
                    content_type = (mimetypes.guess_type(path)[0] or 'text/plain')
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.end_headers()
            if send_body:
                self.wfile.write(body)

        def log_message(self, format: str, *args):
            print(f'preview: {format % args}', file=sys.stderr)

    return PreviewHandler


def export_preview(root: Path, destination: Path) -> Path:
    root, destination = root.resolve(), destination.resolve()
    if destination == root or root.is_relative_to(destination):
        raise ValueError('Output directory must not be the repository root or its parent')
    if destination.is_relative_to(root):
        first = destination.relative_to(root).parts[0]
        if first in {'data', 'docs', 'assets', 'scripts', 'schemas', 'templates', 'tests', '.github', '.git', '.venv'}:
            raise ValueError('Output must not overlap a source directory; use .preview instead')
    # Generate before writing so invalid catalog data cannot damage a prior snapshot.
    source = catalog_markdown(root)
    destination.mkdir(parents=True, exist_ok=True)
    index = render_page(source, 'assets/preview.css')
    (destination / 'index.html').write_text(index, encoding='utf-8')
    (destination / 'README.html').write_text(index, encoding='utf-8')
    candidates = [root / name for name in ROOT_FILES - {'README.md'}]
    candidates += [root / 'data/README.md', root / 'data/taxonomy.json', root / 'data/resources.json']
    candidates += list((root / 'data/papers').glob('*.json'))
    candidates += list((root / 'schemas').glob('*.schema.json'))
    candidates += list((root / 'docs').rglob('*.md'))
    candidates += list((root / 'assets').rglob('*'))
    for path in candidates:
        relative = path.relative_to(root).as_posix()
        if allowed_file(root, relative) is None:
            continue
        target = destination / relative
        if path.suffix == '.md':
            target = target.with_suffix('.html')
        target.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == '.md':
            stylesheet = os.path.relpath(destination / 'assets/preview.css', target.parent)
            target.write_text(render_page(path.read_text(encoding='utf-8'), stylesheet), encoding='utf-8')
        else:
            shutil.copyfile(path, target)
    return destination / 'index.html'


def main(argv: list[str] | None = None) -> int:
    from catalog import CatalogError

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--port', type=int, default=8766)
    parser.add_argument('--output', type=Path, help='Export an HTML directory instead of starting a server')
    args = parser.parse_args(argv)
    try:
        if args.output:
            destination = args.output if args.output.is_absolute() else args.root / args.output
            print(export_preview(args.root, destination))
            return 0
        catalog_markdown(args.root)
        with ThreadingHTTPServer(('127.0.0.1', args.port), make_handler(args.root)) as server:
            print(f'Preview: http://127.0.0.1:{server.server_port}/ (Ctrl+C to stop)', flush=True)
            print('Refresh after editing source files. This preview approximates GitHub rendering.', flush=True)
            server.serve_forever()
    except KeyboardInterrupt:
        return 0
    except (CatalogError, OSError, ValueError) as error:
        print(f'Preview failed: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
