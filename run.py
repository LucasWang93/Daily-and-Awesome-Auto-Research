#!/usr/bin/env python3
"""Daily Papers Assistant - main entry point."""

import argparse
from pathlib import Path

import yaml

from src.collector import collect_all
from src.llm import LLMClient
from src.ranker import rank_papers
from src.archiver import archive_papers
from src.summarizer import generate_report
from src.notifier import send_email
from src.utils import get_logger

PROJECT_DIR = Path(__file__).resolve().parent
LOGGER = get_logger("daily_papers", log_dir=PROJECT_DIR / "logs")


def load_config(path=None):
    cfg_path = Path(path) if path else PROJECT_DIR / "config.yaml"
    with open(cfg_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Daily Papers Assistant")
    parser.add_argument("--config", type=str, default=None, help="Path to config.yaml")
    parser.add_argument("--dry-run", action="store_true", help="Collect and rank only")
    args = parser.parse_args()

    cfg = load_config(args.config)
    topics = cfg["topics"]
    LOGGER.info("=== Daily Papers Assistant started ===")
    LOGGER.info("Topics: %s", topics)

    LOGGER.info("--- Step 1: Collecting papers ---")
    papers = collect_all(
        keywords=topics,
        arxiv_cfg=cfg["sources"].get("arxiv", {}),
        nature_cfg=cfg["sources"].get("nature", {}),
        hf_cfg=cfg["sources"].get("huggingface", {}),
    )
    LOGGER.info("Collected %d papers total", len(papers))

    if not papers:
        LOGGER.warning("No papers found. Exiting.")
        return

    LOGGER.info("--- Step 2: Ranking papers with GPT-5 ---")
    llm_cfg = cfg.get("llm", {})
    llm = LLMClient(
        model=llm_cfg.get("model", "gpt-5"),
        temperature=llm_cfg.get("temperature", 0.3),
        max_tokens=llm_cfg.get("max_tokens", 4096),
    )

    ranking_cfg = cfg.get("ranking", {})
    top_k = ranking_cfg.get("top_k", 20)
    top_papers = rank_papers(papers, topics, llm, top_k=top_k)
    LOGGER.info("Top %d papers selected", len(top_papers))

    if args.dry_run:
        LOGGER.info("--- Dry run mode ---")
        for i, p in enumerate(top_papers, 1):
            sc = p.get("scores", {})
            LOGGER.info("  #%d [%.2f] %s", i, sc.get("composite", 0), p["title"][:80])
        return

    LOGGER.info("--- Step 3: Archiving important papers ---")
    archive_dir = PROJECT_DIR / cfg["output"].get("archive_dir", "archive")
    archive_max = ranking_cfg.get("archive_max", 5)
    archived = archive_papers(top_papers, llm, archive_dir, topics, archive_max=archive_max)
    LOGGER.info("Archived %d papers", len(archived))

    LOGGER.info("--- Step 4: Generating daily report ---")
    reports_dir = PROJECT_DIR / cfg["output"].get("reports_dir", "reports")
    report_path = generate_report(top_papers, llm, reports_dir, archived_summaries=archived)
    LOGGER.info("Report generated: %s", report_path)

    LOGGER.info("--- Step 5: Email notification ---")
    send_email(report_path, cfg.get("email", {}))

    LOGGER.info("=== Daily Papers Assistant completed ===")


if __name__ == "__main__":
    main()
