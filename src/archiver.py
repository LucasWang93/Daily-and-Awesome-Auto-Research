"""Archive truly important papers: GPT-5 importance judgment, PDF download, deep summary."""

import json
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from .llm import LLMClient
from .utils import get_logger

LOGGER = get_logger(__name__)

IMPORTANCE_SYSTEM = (
    "You are a senior AI researcher. Evaluate whether the following papers are "
    "TRULY IMPORTANT -- meaning they represent a breakthrough innovation, a "
    "significant methodological contribution, or could have major impact on the field.\n\n"
    "Be selective and strict. Most papers are incremental; only flag those that are "
    "genuinely important.\n\n"
    "For each paper, return:\n"
    '- "paper_id": string\n'
    '- "important": boolean (true only if truly important)\n'
    '- "importance_reason": 1-2 sentence justification\n\n'
    'Return a JSON object with key "judgments" containing an array of the above.\n'
    "Return ONLY valid JSON."
)

DEEP_SUMMARY_SYSTEM = (
    "You are a world-class AI research analyst. Write a deep, high-quality summary "
    "of the following paper IN CHINESE (500-800 characters). Cover:\n\n"
    "1. Research motivation and the problem being solved\n"
    "2. Core methodology and technical innovations\n"
    "3. Key experimental results and findings\n"
    "4. How this work differs from existing approaches\n"
    "5. Potential impact and future directions\n\n"
    "Write in clear, professional Chinese suitable for an expert audience. "
    "Output the summary text directly, no JSON wrapping."
)

METADATA_FILE = "metadata.json"


def _download_pdf(url, dest_path, timeout=60):
    """Download a PDF file. Returns True on success."""
    if not url:
        return False
    try:
        req = Request(url, headers={
            "User-Agent": "DailyPapersAssistant/1.0 (academic research tool)",
        })
        with urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        dest_path.write_bytes(data)
        LOGGER.info("Downloaded PDF: %s (%d bytes)", dest_path.name, len(data))
        return True
    except (URLError, TimeoutError, OSError) as exc:
        LOGGER.warning("PDF download failed for %s: %s", url, exc)
        return False


def judge_importance(papers, llm, archive_max=5):
    """Use GPT-5 to judge which papers are truly important (max archive_max)."""
    if not papers:
        return []

    paper_descs = []
    for p in papers:
        sc = p.get("scores", {})
        paper_descs.append(
            f"ID: {p['paper_id']}\n"
            f"Title: {p['title']}\n"
            f"Abstract: {p['abstract'][:800]}\n"
            f"Scores: rel={sc.get('relevance')}, nov={sc.get('novelty')}, "
            f"imp={sc.get('impact')}, comp={sc.get('composite')}\n"
            f"Reason: {sc.get('reason', '')}\n"
        )
    user_prompt = "\n---\n".join(paper_descs)

    try:
        result = llm.generate_json(IMPORTANCE_SYSTEM, user_prompt, max_tokens=2048)
    except Exception as exc:
        LOGGER.error("Importance judgment LLM call failed: %s", exc)
        return []

    judgments = result.get("judgments", [])
    important_ids = []
    for j in judgments:
        if j.get("important") and len(important_ids) < archive_max:
            important_ids.append({
                "paper_id": j["paper_id"],
                "importance_reason": j.get("importance_reason", ""),
            })

    LOGGER.info(
        "Importance judgment: %d/%d papers marked as truly important",
        len(important_ids), len(papers),
    )
    return important_ids


def _generate_deep_summary(paper, llm):
    """Generate a deep Chinese summary for a single paper."""
    user_prompt = (
        f"Title: {paper['title']}\n"
        f"Authors: {', '.join(paper['authors'][:5])}\n"
        f"Abstract: {paper['abstract']}\n"
        f"Source: {paper['source']}\n"
        f"URL: {paper['url']}\n"
    )
    try:
        return llm.generate(
            DEEP_SUMMARY_SYSTEM, user_prompt,
            temperature=0.4, max_tokens=2048,
        )
    except Exception as exc:
        LOGGER.error("Deep summary generation failed for %s: %s", paper["paper_id"], exc)
        return ""


def _pick_topic(paper, topics):
    """Pick the best-matching topic directory for this paper."""
    matched = paper.get("keywords_matched", [])
    if matched:
        return matched[0].replace(" ", "_").lower()
    title_abs = (paper.get("title", "") + " " + paper.get("abstract", "")).lower()
    for t in topics:
        if t.lower() in title_abs:
            return t.replace(" ", "_").lower()
    return "general"


def _load_metadata(archive_dir):
    meta_path = Path(archive_dir) / METADATA_FILE
    if meta_path.exists():
        try:
            return json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    return []


def _save_metadata(archive_dir, metadata):
    meta_path = Path(archive_dir) / METADATA_FILE
    meta_path.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def archive_papers(top_papers, llm, archive_dir, topics, archive_max=5):
    """Judge importance, archive truly important papers with deep summaries.

    Returns list of archived paper info dicts (for inclusion in the report).
    """
    archive_dir = Path(archive_dir)
    archive_dir.mkdir(parents=True, exist_ok=True)

    important = judge_importance(top_papers, llm, archive_max=archive_max)
    if not important:
        LOGGER.info("No papers judged as truly important today.")
        return []

    important_ids = {item["paper_id"]: item for item in important}
    papers_to_archive = [p for p in top_papers if p["paper_id"] in important_ids]

    existing_meta = _load_metadata(archive_dir)
    existing_ids = {m["paper_id"] for m in existing_meta}

    archived = []
    for paper in papers_to_archive:
        pid = paper["paper_id"]
        if pid in existing_ids:
            LOGGER.info("Paper %s already archived, skipping", pid)
            continue

        topic_dir = _pick_topic(paper, topics)
        safe_pid = pid.replace("/", "_")
        paper_dir = archive_dir / topic_dir / safe_pid
        paper_dir.mkdir(parents=True, exist_ok=True)

        # Download PDF
        pdf_path = paper_dir / f"{safe_pid}.pdf"
        pdf_ok = _download_pdf(paper.get("pdf_url", ""), pdf_path)

        # Generate deep summary
        LOGGER.info("Generating deep summary for: %s", paper["title"][:80])
        deep_summary = _generate_deep_summary(paper, llm)

        summary_path = paper_dir / "summary.md"
        summary_content = (
            f"# {paper['title']}\n\n"
            f"- **Paper ID**: {pid}\n"
            f"- **Authors**: {', '.join(paper['authors'][:5])}\n"
            f"- **Source**: {paper['source']}\n"
            f"- **Date**: {paper['date']}\n"
            f"- **URL**: {paper['url']}\n"
            f"- **PDF**: {'downloaded' if pdf_ok else paper.get('pdf_url', 'N/A')}\n\n"
            f"## Deep Summary\n\n{deep_summary}\n"
        )
        summary_path.write_text(summary_content, encoding="utf-8")

        # Save paper metadata JSON
        meta_entry = {
            "paper_id": pid,
            "title": paper["title"],
            "authors": paper["authors"],
            "url": paper["url"],
            "date": paper["date"],
            "source": paper["source"],
            "topic": topic_dir,
            "scores": paper.get("scores", {}),
            "importance_reason": important_ids[pid].get("importance_reason", ""),
            "pdf_downloaded": pdf_ok,
            "archive_path": str(paper_dir),
        }

        paper_meta_path = paper_dir / "meta.json"
        paper_meta_path.write_text(
            json.dumps(meta_entry, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        existing_meta.append(meta_entry)
        archived.append({
            "paper_id": pid,
            "title": paper["title"],
            "url": paper["url"],
            "deep_summary": deep_summary,
        })

        LOGGER.info("Archived: %s -> %s", pid, paper_dir)
        time.sleep(0.5)

    _save_metadata(archive_dir, existing_meta)
    LOGGER.info("Archival complete: %d papers archived today", len(archived))
    return archived
