"""Generate digest-style Markdown reports from ranked or archived papers."""

from datetime import datetime, timezone
from pathlib import Path

from .utils import get_logger

LOGGER = get_logger(__name__)


def _paper_line(paper: dict) -> str:
    summary = paper.get("summary")
    if isinstance(summary, list):
        summary_text = " ".join(summary[:2])
    else:
        summary_text = paper.get("reason", "")
    return (
        f"## {paper['title']}\n\n"
        f"- ID: `{paper.get('paper_id', paper.get('id', ''))}`\n"
        f"- Score: {paper.get('importance_score', paper.get('scores', {}).get('composite', 'n/a'))}\n"
        f"- Themes: {', '.join(paper.get('theme_names', paper.get('themes', [])))}\n"
        f"- Link: {paper.get('links', {}).get('paper', paper.get('url', ''))}\n\n"
        f"{summary_text}\n"
    )


def generate_report(papers, reports_dir, archived_summaries=None, report_title="Daily Auto-Research Digest"):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report_path = Path(reports_dir) / f"{today}.md"
    Path(reports_dir).mkdir(parents=True, exist_ok=True)

    archived_summaries = archived_summaries or []
    lines = [
        f"# {report_title} - {today}",
        "",
        "This digest tracks recent additions to the auto-research knowledge base.",
        "",
    ]

    if papers:
        lines.extend(["## Ranked Candidates", ""])
        for paper in papers:
            lines.append(_paper_line(paper))
            lines.append("")

    if archived_summaries:
        lines.extend(["## Newly Archived Cards", ""])
        for paper in archived_summaries:
            lines.append(_paper_line(paper))
            lines.append("")

    if not papers and not archived_summaries:
        lines.append("No new additions today.")

    report_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    LOGGER.info("Report saved to %s", report_path)
    return report_path
