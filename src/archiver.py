"""Archive high-signal papers as Markdown knowledge cards."""

import json
from datetime import datetime, timezone
from pathlib import Path

from .utils import get_logger

LOGGER = get_logger(__name__)

CARD_SUMMARY_SYSTEM = (
    "You are writing a concise research card for an awesome repository about auto-research.\n"
    "Return valid JSON with keys:\n"
    '- "summary_short": array of 3 to 5 short bullet strings\n'
    '- "why_it_matters": one short paragraph\n'
    '- "digest_summary": a 2 to 4 sentence English summary suitable for a daily newsletter\n'
    '- "editor_note": one optional sentence on why it matters today\n'
    '- "code_repos": array of repo URL strings if clearly mentioned, else empty array\n'
    "Use English. Keep claims grounded in the provided title and abstract."
)


def _slugify(value: str) -> str:
    import re

    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def _write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def _build_card_content(paper: dict) -> str:
    bullet_lines = "\n".join(f"- {line}" for line in paper.get("summary_short", []))
    theme_lines = ", ".join(paper.get("theme_names", paper.get("themes", [])))
    code_lines = ""
    if paper.get("code_repos"):
        code_lines = "\n".join(f"- {repo}" for repo in paper["code_repos"])
    else:
        code_lines = "- None linked yet"
    sources = ", ".join(paper.get("sources", [paper.get("source", "unknown")]))
    return (
        f"# {paper['title']}\n\n"
        f"## Snapshot\n\n"
        f"- Paper ID: `{paper['paper_id']}`\n"
        f"- Date: {paper.get('date', '')}\n"
        f"- Themes: {theme_lines}\n"
        f"- Sources: {sources}\n"
        f"- Importance Score: {paper.get('importance_score', 0)}\n"
        f"- Featured: {'yes' if paper.get('featured') else 'no'}\n\n"
        f"## Links\n\n"
        f"- Paper: {paper['links'].get('paper', paper.get('url', ''))}\n"
        f"- ArXiv: {paper['links'].get('arxiv', '')}\n"
        f"- PDF: {paper['links'].get('pdf', '')}\n"
        f"- HuggingFace: {paper['links'].get('huggingface', '')}\n\n"
        f"## Summary\n\n"
        f"{bullet_lines}\n\n"
        f"## Why It Matters\n\n"
        f"{paper.get('why_it_matters', '')}\n\n"
        f"## Daily Digest Summary\n\n"
        f"{paper.get('digest_summary', '')}\n\n"
        f"## Related Repos\n\n"
        f"{code_lines}\n"
    )


def _generate_card_fields(paper: dict, llm) -> tuple[list[str], str, str, str, list[str]]:
    prompt = (
        f"Title: {paper['title']}\n"
        f"Abstract: {paper['abstract']}\n"
        f"Themes: {', '.join(paper.get('theme_names', paper.get('themes', [])))}\n"
        f"Links: {paper.get('url', '')}\n"
    )
    try:
        result = llm.generate_json(CARD_SUMMARY_SYSTEM, prompt, temperature=0.2, max_tokens=1200)
    except Exception as exc:
        LOGGER.error("Card summary generation failed for %s: %s", paper["paper_id"], exc)
        fallback_bullets = [
            paper["title"],
            f"Classified under {', '.join(paper.get('theme_names', paper.get('themes', [])))}",
            f"Source: {paper.get('source', 'unknown')}",
        ]
        fallback_digest = paper.get("scores", {}).get("reason", "")
        return fallback_bullets, fallback_digest, fallback_digest, "", []

    return (
        result.get("summary_short", []),
        result.get("why_it_matters", ""),
        result.get("digest_summary", ""),
        result.get("editor_note", ""),
        result.get("code_repos", []),
    )


def archive_papers(top_papers: list[dict], llm, archive_dir: Path, archive_cfg: dict | None = None) -> list[dict]:
    archive_cfg = archive_cfg or {}
    archive_dir = Path(archive_dir)
    papers_dir = archive_dir / "papers"
    metadata_path = archive_dir / "metadata.json"
    existing_meta = _load_json(metadata_path, [])
    existing_ids = {entry["id"] for entry in existing_meta if "id" in entry}

    archive_threshold = archive_cfg.get("min_score", 7.5)
    archive_max = archive_cfg.get("archive_max", 8)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    today_dir = papers_dir / today
    today_dir.mkdir(parents=True, exist_ok=True)

    archived = []
    for paper in top_papers:
        if len(archived) >= archive_max:
            break
        score = paper.get("scores", {}).get("composite", 0)
        if score < archive_threshold:
            continue
        if paper["paper_id"] in existing_ids:
            continue

        summary_short, why_it_matters, digest_summary, editor_note, code_repos = _generate_card_fields(paper, llm)
        featured = bool(paper.get("scores", {}).get("featured")) or score >= archive_cfg.get("featured_min_score", 8.8)
        record = {
            "id": paper["paper_id"],
            "paper_id": paper["paper_id"],
            "title": paper["title"],
            "summary_short": summary_short,
            "date": paper.get("date", today),
            "source": paper.get("source", "unknown"),
            "sources": paper.get("sources", [paper.get("source", "unknown")]),
            "themes": paper.get("themes", []),
            "theme_names": paper.get("theme_names", []),
            "importance_score": round(score, 2),
            "reason": paper.get("scores", {}).get("reason", ""),
            "links": paper.get("links", {}),
            "code_repos": code_repos,
            "featured": featured,
            "why_it_matters": why_it_matters,
            "digest_summary": digest_summary,
            "editor_note": editor_note,
        }
        card_path = today_dir / f"{paper.get('slug') or _slugify(paper['paper_id'])}.md"
        card_path.write_text(_build_card_content(record), encoding="utf-8")
        record["archive_path"] = str(card_path.relative_to(archive_dir.parent))
        existing_meta.append(record)
        existing_ids.add(record["id"])
        archived.append(record)
        LOGGER.info("Archived paper card: %s", card_path)

    _write_json(metadata_path, existing_meta)
    LOGGER.info("Archival complete: %d papers archived", len(archived))
    return archived
