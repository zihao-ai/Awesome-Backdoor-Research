#!/usr/bin/env python3
"""Validate catalog data and template locally, without changing files."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from catalog import CatalogError, ROOT, load_catalog


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root (default: this checkout)")
    args = parser.parse_args(argv)
    try:
        catalog = load_catalog(args.root)
    except CatalogError as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    areas = catalog["taxonomy"]["areas"]
    count = sum(len(area["topics"]) for area in areas)
    resources = sum(len(items) for items in catalog["resources"].values())
    print(f"Valid: {len(areas)} areas, {count} subcategories, {len(catalog['papers'])} papers, {resources} resources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
