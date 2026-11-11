#!/usr/bin/env python3
"""Normalise the domain column and drop duplicate companies.

Usage:
    python3 clean_companies.py outputs/companies.csv

Rewrites the file in place. Keeps the first row for each normalised domain.
Needs only the Python standard library.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import urlparse


def normalise_domain(value: str) -> str:
    text = (value or "").strip().lower()
    if not text:
        return ""
    if "://" not in text:
        text = "https://" + text
    parsed = urlparse(text)
    host = parsed.netloc or parsed.path.split("/")[0]
    if host.startswith("www."):
        host = host[4:]
    return host.strip().strip(".")


def clean(path: Path) -> tuple[int, int]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        if not fieldnames or "domain" not in fieldnames:
            raise SystemExit("The CSV needs a header row with a 'domain' column.")
        rows = list(reader)

    kept = []
    seen = set()
    dropped = 0
    for row in rows:
        domain = normalise_domain(row.get("domain", ""))
        row["domain"] = domain
        if "linkedin_url" in row:
            linkedin = normalise_domain(row.get("linkedin_url", ""))
            # Keep the path for LinkedIn URLs (company slug).
            raw = (row.get("linkedin_url") or "").strip().lower()
            if raw:
                if "://" not in raw:
                    raw = "https://" + raw
                parsed = urlparse(raw)
                host = parsed.netloc or ""
                if host.startswith("www."):
                    host = host[4:]
                path_part = parsed.path.rstrip("/")
                row["linkedin_url"] = f"{host}{path_part}" if host else path_part.lstrip("/")
        if not domain:
            dropped += 1
            continue
        if domain in seen:
            dropped += 1
            continue
        seen.add(domain)
        kept.append(row)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(kept)

    return len(kept), dropped


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 clean_companies.py outputs/companies.csv")
    path = Path(sys.argv[1])
    if not path.is_file():
        raise SystemExit(f"File not found: {path}")
    kept, dropped = clean(path)
    print(f"Kept {kept} companies. Removed {dropped} empty or duplicate domain rows.")


if __name__ == "__main__":
    main()
