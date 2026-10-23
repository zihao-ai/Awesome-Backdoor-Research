#!/usr/bin/env python3
"""Explicit, bounded URL audit. This is not paper-metadata verification."""
from __future__ import annotations

import argparse
from http.client import HTTPException
from concurrent.futures import ThreadPoolExecutor
import json
import math
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


class BoundedRedirects(HTTPRedirectHandler):
    max_redirections = 5
    max_repeats = 2


def collect_urls(catalog: dict) -> list[str]:
    urls = []
    for paper in catalog['papers']:
        urls.append(paper['url'])
        if paper.get('code'):
            urls.append(paper['code'])
    for group in catalog['resources'].values():
        for resource in group:
            urls.append(resource['url'])
            urls.extend(link['url'] for link in resource.get('links', []))
    return sorted({urldefrag(url)[0] for url in urls})


def check_url(url: str, timeout: float) -> dict:
    result = {'url': url, 'status': 'unreachable', 'http_status': None,
              'final_url': url, 'detail': ''}
    parts = urlsplit(url)
    if parts.scheme not in ('http', 'https') or not parts.hostname:
        result['detail'] = 'Only absolute HTTP(S) URLs are supported.'
        return result
    opener = build_opener(BoundedRedirects())
    for method in ('HEAD', 'GET'):
        request = Request(url, method=method, headers={
            'User-Agent': 'Awesome-Backdoor-Research-Link-Checker/1.0',
            'Accept': '*/*'})
        # GET fallback reads no response body, so PDF/download size is irrelevant.
        try:
            with opener.open(request, timeout=timeout) as response:
                result.update(http_status=response.status, final_url=response.url,
                              status='ok', detail=f'{method} succeeded')
            return result
        except HTTPError as error:
            status = error.code
            result.update(http_status=status, final_url=error.url)
            error.close()
            if method == 'HEAD' and status in (403, 405, 501):
                continue
            if status in (401, 403, 429):
                result['status'] = 'blocked'
            elif status in (404, 410):
                result['status'] = 'broken'
            else:
                result['status'] = 'unreachable'
            result['detail'] = f'{method} returned HTTP {status}'
            return result
        except (HTTPException, URLError, TimeoutError, OSError, ValueError) as error:
            result['detail'] = f'{method}: {error}'
            return result
    return result


def audit_links(urls: list[str], timeout: float = 10, workers: int = 4) -> list[dict]:
    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError('timeout must be a finite positive number')
    if not 1 <= workers <= 32:
        raise ValueError('workers must be between 1 and 32')
    unique = sorted({urldefrag(url)[0] for url in urls})
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(lambda url: check_url(url, timeout), unique))


def exit_status(results: list[dict], strict: bool = False) -> int:
    if any(row['status'] == 'broken' for row in results):
        return 1
    if strict and any(row['status'] != 'ok' for row in results):
        return 2
    return 0


def main(argv: list[str] | None = None) -> int:
    from catalog import CatalogError, ROOT, load_catalog

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--list', action='store_true', help='List source URLs without network requests')
    parser.add_argument('--timeout', type=float, default=10, help='Per-request socket timeout in seconds')
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--strict', action='store_true', help='Also fail on blocked/unreachable URLs')
    parser.add_argument('--report', type=Path, default=Path('reports/links.json'))
    args = parser.parse_args(argv)
    try:
        urls = collect_urls(load_catalog(args.root))
        if args.list:
            print('\n'.join(urls))
            return 0
        results = audit_links(urls, args.timeout, args.workers)
        counts = {status: sum(r['status'] == status for r in results)
                  for status in ('ok', 'broken', 'blocked', 'unreachable')}
        report = args.report if args.report.is_absolute() else args.root / args.report
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps({'counts': counts, 'results': results}, indent=2) + '\n', encoding='utf-8')
        for row in results:
            print(f"{row['status']:11} {row['url']} ({row['detail']})")
        print(f"Summary: {counts}; report: {report}")
        print('Blocked/unreachable URLs need manual review; HTTP errors do not invalidate the paper.')
        return exit_status(results, args.strict)
    except (CatalogError, OSError, ValueError) as error:
        print(f'Link audit failed: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
