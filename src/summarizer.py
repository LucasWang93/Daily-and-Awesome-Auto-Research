"""Generate daily Top-20 summary report in Markdown (Chinese)."""

from datetime import datetime, timezone
from pathlib import Path

from .llm import LLMClient
from .utils import get_logger

LOGGER = get_logger(__name__)

SUMMARY_SYSTEM = (
    "You are an expert scientific communicator writing for Chinese-speaking "
    "AI researchers. Given a ranked list of today's top papers, produce a "
    "Markdown report IN CHINESE.\n\n"
    "STRUCTURE:\n"
    "1. Title: # Daily Papers Report - {date}\n"
    "2. ## Today Highlights: 3-5 sentences on key trends.\n"
    "3. ## Top Papers: numbered list of ALL papers (do NOT skip any).\n"
    "   For each paper:\n"
    "   - Title (English), Authors (first 3 + et al.), Source, Date\n"
    "   - Composite score (relevance/novelty/impact)\n"
    "   - 2-3 sentence Chinese summary\n"
    "   - Link\n\n"
    "CRITICAL RULES:\n"
    "- You MUST include ALL papers. NEVER skip, truncate, or abbreviate.\n"
    "- Output raw Markdown. NO code fences (no triple backticks).\n"
    "- Write in professional Chinese."
)


def _build_paper_block(papers):
    lines = []
    for i, p in enumerate(papers, 1):
        sc = p.get("scores", {})
        au = ", ".join(p["authors"][:3])
        if len(p["authors"]) > 3:
            au += " et al."
        lines.append(
            f"--- Paper {i} ---\n"
            f"ID: {p['paper_id']}\n"
            f"Title: {p['title']}\n"
            f"Authors: {au}\n"
            f"Source: {p['source']}  Date: {p['date']}\n"
            f"Scores: rel={sc.get('relevance', '?')}, "
            f"nov={sc.get('novelty', '?')}, "
            f"imp={sc.get('impact', '?')}, "
            f"comp={sc.get('composite', '?')}\n"
            f"Reason: {sc.get('reason', '')}\n"
            f"Abstract: {p['abstract'][:600]}\n"
            f"URL: {p['url']}\n"
        )
    return "\n".join(lines)


def _strip_code_fences(text):
    """Remove wrapping code fences if LLM adds them."""
    text = text.strip()
    fence = chr(96) * 3
    for prefix in [fence + "markdown\n", fence + "md\n", fence + "\n"]:
        if text.startswith(prefix):
            text = text[len(prefix):]
            break
    if text.endswith(fence):
        text = text[:-3].rstrip()
    return text


def generate_report(papers, llm, reports_dir, archived_summaries=None):
    """Generate daily Markdown report and save to reports_dir."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report_path = Path(reports_dir) / f"{today}.md"
    Path(reports_dir).mkdir(parents=True, exist_ok=True)

    if not papers:
        report_path.write_text(
            f"# Daily Papers Report - {today}\n\n"
            "No relevant papers found today.\n",
            encoding="utf-8",
        )
        LOGGER.info("Empty report saved to %s", report_path)
        return report_path

    system = SUMMARY_SYSTEM.format(date=today)
    user_content = f"Today: {today}\n\nTotal papers: {len(papers)}. List ALL of them.\n\n" + _build_paper_block(papers)

    LOGGER.info("Generating summary report for %d papers...", len(papers))
    report_md = llm.generate(system, user_content, max_tokens=8192)
    report_md = _strip_code_fences(report_md)

    if archived_summaries:
        section = "\n\n## Archived Papers - Deep Dive\n\n"
        for a in archived_summaries:
            section += f"### {a['title']}\n\n"
            section += f"- **Paper ID**: {a['paper_id']}\n"
            section += f"- **URL**: {a['url']}\n\n"
            section += a.get("deep_summary", "") + "\n\n---\n\n"
        report_md += section

    report_path.write_text(report_md, encoding="utf-8")
    LOGGER.info("Report saved to %s (%d chars)", report_path, len(report_md))
    return report_path
