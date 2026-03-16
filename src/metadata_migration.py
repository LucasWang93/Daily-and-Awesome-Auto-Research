"""Helpers for normalizing legacy archive metadata records."""

from __future__ import annotations


def _normalize_topic_name(value: str) -> str:
    return value.replace("_", " ").strip() if value else "unclassified"


def _normalize_archive_path(value: str) -> str:
    if not value:
        return ""
    marker = "/archive/"
    if marker in value:
        return value[value.index(marker) + 1:]
    return value


def _normalize_links(record: dict) -> dict:
    links = record.get("links")
    if isinstance(links, dict) and links:
        merged = dict(links)
    else:
        merged = {}

    paper_url = merged.get("paper") or record.get("url", "")
    paper_id = record.get("paper_id", record.get("id", ""))

    merged.setdefault("paper", paper_url)
    if paper_id:
        merged.setdefault("arxiv", f"https://arxiv.org/abs/{paper_id}")
        merged.setdefault("pdf", f"https://arxiv.org/pdf/{paper_id}")
    return merged


def normalize_archive_record(record: dict) -> dict:
    normalized = dict(record)
    normalized["id"] = record.get("id", record.get("paper_id", ""))
    normalized["paper_id"] = record.get("paper_id", normalized["id"])
    normalized["links"] = _normalize_links(record)

    themes = record.get("themes")
    if not isinstance(themes, list) or not themes:
        topic = record.get("topic")
        normalized["themes"] = [topic] if topic else ["unclassified"]
    else:
        normalized["themes"] = themes

    theme_names = record.get("theme_names")
    if not isinstance(theme_names, list) or not theme_names:
        normalized["theme_names"] = [_normalize_topic_name(theme) for theme in normalized["themes"]]
    else:
        normalized["theme_names"] = theme_names

    normalized["importance_score"] = record.get(
        "importance_score",
        record.get("scores", {}).get("composite", 0),
    )
    normalized["why_it_matters"] = record.get(
        "why_it_matters",
        record.get("importance_reason", record.get("reason", "")),
    )
    normalized["summary_short"] = record.get("summary_short", record.get("summary", []))
    normalized["digest_summary"] = record.get(
        "digest_summary",
        record.get("why_it_matters", record.get("importance_reason", record.get("reason", ""))),
    )
    normalized["editor_note"] = record.get("editor_note", "")
    normalized["featured"] = bool(record.get("featured", False))
    normalized["archive_path"] = _normalize_archive_path(record.get("archive_path", ""))
    return normalized
