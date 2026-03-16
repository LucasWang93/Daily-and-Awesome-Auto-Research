#!/usr/bin/env python3
"""Normalize legacy archive/metadata.json records in place."""

import json
from pathlib import Path

from src.metadata_migration import normalize_archive_record


def main() -> None:
    project_dir = Path(__file__).absolute().parent
    metadata_path = project_dir / "archive" / "metadata.json"
    if not metadata_path.exists():
        print(f"metadata file not found: {metadata_path}")
        return

    records = json.loads(metadata_path.read_text(encoding="utf-8"))
    normalized = [normalize_archive_record(record) for record in records]
    metadata_path.write_text(
        json.dumps(normalized, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Normalized {len(normalized)} archive metadata records: {metadata_path}")


if __name__ == "__main__":
    main()
