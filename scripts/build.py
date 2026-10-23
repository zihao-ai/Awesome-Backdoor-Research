#!/usr/bin/env python3
"""Build README.md from validated sources or check that it is current."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys
import tempfile

from catalog import CatalogError, ROOT, load_catalog
from render import render_readme


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root (default: this checkout)")
    parser.add_argument("--check", action="store_true", help="Fail if README.md is stale; never write files")
    args = parser.parse_args(argv)
    destination = args.root / "README.md"
    temporary: str | None = None
    try:
        catalog = load_catalog(args.root)
        template = (args.root / "templates/README.md").read_text(encoding="utf-8")
        rendered = render_readme(catalog, template)
        current = destination.read_text(encoding="utf-8") if destination.exists() else None
        if args.check:
            if current != rendered:
                print("README.md is stale or missing. Run: python scripts/build.py" + (f" --root {args.root}" if args.root != ROOT else ""), file=sys.stderr)
                return 1
            print("README.md is up to date.")
            return 0
        if current == rendered:
            print("README.md is already up to date.")
            return 0
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=args.root, prefix=".README-", suffix=".tmp", delete=False) as output:
            temporary = output.name
            output.write(rendered)
        os.chmod(temporary, destination.stat().st_mode & 0o777 if destination.exists() else 0o644)
        os.replace(temporary, destination)
        temporary = None
    except (CatalogError, OSError, UnicodeError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    finally:
        if temporary is not None:
            Path(temporary).unlink(missing_ok=True)
    print(f"Generated {destination}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
