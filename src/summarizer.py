"""Generate human-readable editorial daily digests."""

from datetime import datetime, timezone
from pathlib import Path

from .utils import get_logger

LOGGER = get_logger(__name__)

HIGHLIGHTS_SYSTEM = (
    "You are writing the opening section of a daily email digest about auto-research.\n"
    "Write 3 to 6 sentences in natural English.\n"
    "Summarize the main themes across today's archived papers, highlight what changed or stands out, "
    "and keep it readable for a human researcher scanning email.\n"
    "Do not use bullet points."
)

def _build_highlights_prompt(papers: list[dict]) -> str:
    lines = []
    for paper in papers[:10]:
        lines.append(
            f"Title: {paper['title']}\n"
            f"Themes: {', '.join(paper.get('theme_names', paper.get('themes', [])))}\n"
            f"Why it matters: {paper.get('why_it_matters', paper.get('reason', ''))}\n"
            f"Digest: {paper.get('digest_summary', '')}\n"
        )
    return "\n---\n".join(lines)


def _paper_line(paper: dict) -> str:
    summary_text = paper.get("digest_summary") or paper.get("reason", "")
    editor_note = paper.get("editor_note", "")
    note_block = f"\n**Why it matters today:** {editor_note}\n" if editor_note else ""
    return (
        f"## {paper['title']}\n\n"
        f"- ID: `{paper.get('paper_id', paper.get('id', ''))}`\n"
        f"- Score: {paper.get('importance_score', paper.get('scores', {}).get('composite', 'n/a'))}\n"
        f"- Themes: {', '.join(paper.get('theme_names', paper.get('themes', [])))}\n"
        f"- Link: {paper.get('links', {}).get('paper', paper.get('url', ''))}\n\n"
        f"{summary_text}\n"
        f"{note_block}"
    )


def generate_report(papers, llm, reports_dir, archived_summaries=None, report_title="Daily Auto-Research Digest"):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report_path = Path(reports_dir) / f"{today}.md"
    Path(reports_dir).mkdir(parents=True, exist_ok=True)

    archived_summaries = archived_summaries or []
    top_archived = archived_summaries[:10]
    other_archived = archived_summaries[10:]

    if top_archived and llm is not None:
        try:
            highlights = llm.generate(
                HIGHLIGHTS_SYSTEM,
                _build_highlights_prompt(top_archived),
                temperature=0.2,
                max_tokens=800,
            ).strip()
        except Exception as exc:
            LOGGER.error("Highlight generation failed: %s", exc)
            highlights = "Today's archived additions continue to reinforce the repository's focus on practical auto-research systems and infrastructure."
    elif top_archived:
        highlights = "Today's archived additions continue to reinforce the repository's focus on practical auto-research systems and infrastructure."
    else:
        highlights = "No major additions today."

    lines = [
        f"# {report_title} - {today}",
        "",
        "## Today in Auto-Research",
        "",
        highlights,
        "",
    ]

    if top_archived:
        lines.extend(["## Top Papers Today", ""])
        for paper in top_archived:
            lines.append(_paper_line(paper))
            lines.append("")

    if other_archived:
        lines.extend(["## Other Notable Additions", ""])
        for paper in other_archived:
            lines.append(
                f"- [{paper['title']}]({paper.get('links', {}).get('paper', paper.get('url', ''))}): "
                f"{paper.get('editor_note') or paper.get('why_it_matters') or paper.get('reason', '')}"
            )
            lines.append("")

    if archived_summaries:
        latest = archived_summaries[0]
        lines.extend([
            "## Latest Archive Entry",
            "",
            f"[{latest['title']}]({latest.get('links', {}).get('paper', latest.get('url', ''))})"
            f" is the latest archived card. Local path: `{latest.get('archive_path', '')}`",
            "",
        ])

    report_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    LOGGER.info("Report saved to %s", report_path)
    return report_path
