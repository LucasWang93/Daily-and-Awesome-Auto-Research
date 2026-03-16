#!/usr/bin/env python3
"""Awesome Auto-Research - main entry point."""

import argparse
from pathlib import Path

import yaml

from src.archiver import archive_papers
from src.collector import collect_all
from src.curator import build_readme
from src.indexer import sync_indexes
from src.llm import LLMClient
from src.notifier import send_email
from src.ranker import rank_papers
from src.summarizer import generate_report
from src.utils import get_logger

PROJECT_DIR = Path(__file__).absolute().parent
LOGGER = get_logger("daily_papers", log_dir=PROJECT_DIR / "logs")


def load_config(path=None):
    cfg_path = Path(path) if path else PROJECT_DIR / "config.yaml"
    with open(cfg_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _build_llm(cfg):
    llm_cfg = cfg.get("llm", {})
    return LLMClient(
        model=llm_cfg.get("model", "gpt-5"),
        temperature=llm_cfg.get("temperature", 0.2),
        max_tokens=llm_cfg.get("max_tokens", 4096),
    )


def cmd_ingest(cfg, dry_run=False):
    LOGGER.info("=== Awesome Auto-Research ingest started ===")
    papers = collect_all(cfg)
    LOGGER.info("Collected %d candidate papers", len(papers))
    if not papers:
        LOGGER.warning("No candidate papers found. Exiting.")
        return {"papers": [], "archived": [], "report_path": None}

    llm = _build_llm(cfg)
    scoring_cfg = cfg.get("scoring", {})
    ranked = rank_papers(
        papers,
        cfg.get("taxonomy", []),
        llm,
        top_k=scoring_cfg.get("top_k", 25),
        dimensions=scoring_cfg.get("dimensions"),
    )
    if dry_run:
        LOGGER.info("--- Dry run candidates ---")
        for i, paper in enumerate(ranked, 1):
            score = paper.get("scores", {}).get("composite", 0)
            LOGGER.info("  #%d [%.2f] %s", i, score, paper["title"][:100])
        return {"papers": ranked, "archived": [], "report_path": None}

    archive_cfg = cfg.get("archive", {})
    output_cfg = cfg.get("output", {})
    archived = archive_papers(
        ranked,
        llm,
        PROJECT_DIR / output_cfg.get("archive_dir", "archive"),
        archive_cfg=archive_cfg,
    )
    sync_indexes(
        PROJECT_DIR,
        cfg,
        archived_papers=archived,
    )
    build_readme(PROJECT_DIR, cfg)

    report_path = generate_report(
        ranked,
        PROJECT_DIR / output_cfg.get("reports_dir", "reports"),
        archived_summaries=archived,
    )
    send_email(report_path, cfg.get("email", {}))
    LOGGER.info("=== Awesome Auto-Research ingest completed ===")
    return {"papers": ranked, "archived": archived, "report_path": report_path}


def cmd_build_readme(cfg):
    readme_path = build_readme(PROJECT_DIR, cfg)
    LOGGER.info("README updated: %s", readme_path)


def cmd_sync_index(cfg):
    result = sync_indexes(PROJECT_DIR, cfg)
    LOGGER.info(
        "Indexes synced: %d papers, %d repos",
        len(result["papers"]),
        len(result["repos"]),
    )


def cmd_curate_report(cfg):
    output_cfg = cfg.get("output", {})
    reports_dir = PROJECT_DIR / output_cfg.get("reports_dir", "reports")
    data_dir = PROJECT_DIR / output_cfg.get("data_dir", "data")
    index_path = data_dir / "papers.json"
    archived = []
    if index_path.exists():
        import json

        archived = json.loads(index_path.read_text(encoding="utf-8"))
    report_path = generate_report(
        [],
        reports_dir,
        archived_summaries=archived[: cfg.get("readme", {}).get("recent_limit", 8)],
        report_title="Awesome Auto-Research Digest",
    )
    LOGGER.info("Curated report generated: %s", report_path)


def main():
    parser = argparse.ArgumentParser(description="Awesome Auto-Research")
    parser.add_argument("--config", type=str, default=None, help="Path to config.yaml")

    subparsers = parser.add_subparsers(dest="command")

    ingest_parser = subparsers.add_parser("ingest", help="Collect, rank, archive, and refresh curated surfaces")
    ingest_parser.add_argument("--dry-run", action="store_true", help="Collect and rank only")

    subparsers.add_parser("build-readme", help="Rebuild README dynamic sections")
    subparsers.add_parser("sync-index", help="Rebuild data indexes from archive/curated data")
    subparsers.add_parser("curate-report", help="Generate a digest from archived cards")

    args = parser.parse_args()
    command = args.command or "ingest"
    cfg = load_config(args.config)

    if command == "ingest":
        cmd_ingest(cfg, dry_run=getattr(args, "dry_run", False))
    elif command == "build-readme":
        cmd_build_readme(cfg)
    elif command == "sync-index":
        cmd_sync_index(cfg)
    elif command == "curate-report":
        cmd_curate_report(cfg)
    else:
        parser.error(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
