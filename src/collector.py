"""Collect papers from ArXiv and HuggingFace, then map them into taxonomy themes."""

import json
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from typing import Optional
from urllib.error import URLError
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

from .taxonomy import (
    collect_query_terms,
    find_theme_matches,
    get_taxonomy_map,
    normalize_theme_id,
)
from .utils import get_logger

LOGGER = get_logger(__name__)

ARXIV_API_URL = "https://export.arxiv.org/api/query"
HF_DAILY_URL = "https://huggingface.co/api/daily_papers"


def _http_get(url: str, retries: int = 3, timeout: int = 30) -> Optional[str]:
    for attempt in range(retries):
        try:
            req = Request(url, headers={
                "User-Agent": "AwesomeAutoResearch/1.0 (academic research curation)",
            })
            with urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8")
        except (URLError, TimeoutError, OSError) as exc:
            LOGGER.warning("HTTP GET %s attempt %d failed: %s", url, attempt + 1, exc)
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    return None


def _slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _build_links(paper_id: str, source_url: str, pdf_url: str) -> dict:
    return {
        "paper": source_url,
        "pdf": pdf_url,
        "arxiv": f"https://arxiv.org/abs/{paper_id}" if paper_id else source_url,
    }


def collect_arxiv(queries: list[str], max_results_per_query: int = 20, days_lookback: int = 3) -> list[dict]:
    papers: list[dict] = []
    seen_ids: set[str] = set()
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_lookback)

    for query_term in queries:
        query = quote_plus(f'all:"{query_term}"')
        url = (
            f"{ARXIV_API_URL}?search_query={query}"
            f"&start=0&max_results={max_results_per_query}"
            f"&sortBy=submittedDate&sortOrder=descending"
        )
        raw = _http_get(url)
        if not raw:
            continue

        try:
            root = ET.fromstring(raw)
        except ET.ParseError:
            LOGGER.error("ArXiv XML parse error for query: %s", query_term)
            continue

        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall("atom:entry", ns):
            pub_el = entry.find("atom:published", ns)
            if pub_el is None or pub_el.text is None:
                continue
            try:
                pub_date = datetime.fromisoformat(pub_el.text.replace("Z", "+00:00"))
            except ValueError:
                continue
            if pub_date < cutoff:
                continue

            id_el = entry.find("atom:id", ns)
            title_el = entry.find("atom:title", ns)
            summary_el = entry.find("atom:summary", ns)
            if id_el is None or not id_el.text or title_el is None or not title_el.text:
                continue

            match = re.search(r"abs/(.+)$", id_el.text)
            paper_id = match.group(1) if match else id_el.text
            if paper_id in seen_ids:
                continue

            authors = [
                node.find("atom:name", ns).text
                for node in entry.findall("atom:author", ns)
                if node.find("atom:name", ns) is not None and node.find("atom:name", ns).text
            ]
            title = title_el.text.strip().replace("\n", " ")
            abstract = (summary_el.text or "").strip().replace("\n", " ") if summary_el is not None else ""
            papers.append({
                "paper_id": paper_id,
                "title": title,
                "abstract": abstract,
                "authors": authors,
                "url": f"https://arxiv.org/abs/{paper_id}",
                "pdf_url": f"https://arxiv.org/pdf/{paper_id}",
                "date": pub_date.strftime("%Y-%m-%d"),
                "source": "arxiv",
                "links": _build_links(paper_id, f"https://arxiv.org/abs/{paper_id}", f"https://arxiv.org/pdf/{paper_id}"),
                "slug": _slugify(f"{paper_id}-{title}"),
            })
            seen_ids.add(paper_id)
        time.sleep(1)

    LOGGER.info("ArXiv: collected %d deduplicated entries", len(papers))
    return papers


def collect_huggingface(max_papers: int = 100) -> list[dict]:
    raw = _http_get(HF_DAILY_URL)
    if not raw:
        LOGGER.error("Failed to fetch HuggingFace daily papers")
        return []

    try:
        items = json.loads(raw)
    except json.JSONDecodeError:
        LOGGER.error("HF daily papers: invalid JSON response")
        return []

    papers: list[dict] = []
    for item in items[:max_papers]:
        paper = item.get("paper", item)
        paper_id = paper.get("id", "")
        title = paper.get("title", "").strip()
        abstract = paper.get("summary", paper.get("abstract", "")).strip()
        if not paper_id or not title:
            continue
        authors = [
            a.get("name", a) if isinstance(a, dict) else str(a)
            for a in paper.get("authors", [])
        ]
        published_at = paper.get("publishedAt", paper.get("published", ""))[:10]
        papers.append({
            "paper_id": paper_id,
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "url": f"https://huggingface.co/papers/{paper_id}",
            "pdf_url": f"https://arxiv.org/pdf/{paper_id}",
            "date": published_at,
            "source": "huggingface_daily",
            "links": {
                "paper": f"https://huggingface.co/papers/{paper_id}",
                "arxiv": f"https://arxiv.org/abs/{paper_id}",
                "pdf": f"https://arxiv.org/pdf/{paper_id}",
                "huggingface": f"https://huggingface.co/papers/{paper_id}",
            },
            "slug": _slugify(f"{paper_id}-{title}"),
        })
    LOGGER.info("HuggingFace Daily: collected %d entries", len(papers))
    return papers


def _attach_taxonomy(papers: list[dict], taxonomy: list[dict]) -> list[dict]:
    taxonomy_map = get_taxonomy_map(taxonomy)
    matched = []
    for paper in papers:
        text = f"{paper.get('title', '')}\n{paper.get('abstract', '')}"
        themes = find_theme_matches(text, taxonomy)
        if not themes:
            continue
        theme_ids = [normalize_theme_id(theme["id"]) for theme in themes]
        paper["themes"] = theme_ids
        paper["theme_names"] = [taxonomy_map[theme_id]["name"] for theme_id in theme_ids if theme_id in taxonomy_map]
        paper["keywords_matched"] = sorted({
            keyword
            for theme in themes
            for keyword in theme.get("query_keywords", [])
            if keyword.lower() in text.lower()
        })
        matched.append(paper)
    return matched


def _deduplicate(papers: list[dict]) -> list[dict]:
    merged: dict[str, dict] = {}
    for paper in papers:
        canonical_id = paper["paper_id"]
        existing = merged.get(canonical_id)
        if existing is None:
            merged[canonical_id] = paper
            continue

        existing_sources = set(existing.get("sources", [existing["source"]]))
        existing_sources.add(paper["source"])
        existing["sources"] = sorted(existing_sources)
        existing["themes"] = sorted(set(existing.get("themes", [])) | set(paper.get("themes", [])))
        existing["theme_names"] = sorted(set(existing.get("theme_names", [])) | set(paper.get("theme_names", [])))
        existing["links"] = {**paper.get("links", {}), **existing.get("links", {})}
        if existing["source"] != "arxiv" and paper["source"] == "arxiv":
            existing["source"] = "arxiv"
            existing["url"] = paper["url"]
            existing["pdf_url"] = paper["pdf_url"]
    return list(merged.values())


def collect_all(cfg: dict) -> list[dict]:
    taxonomy = cfg.get("taxonomy", [])
    query_terms = collect_query_terms(taxonomy)
    sources_cfg = cfg.get("sources", {})

    papers: list[dict] = []
    arxiv_cfg = sources_cfg.get("arxiv", {})
    if arxiv_cfg.get("enabled", True):
        papers.extend(
            collect_arxiv(
                query_terms,
                max_results_per_query=arxiv_cfg.get("max_per_query", arxiv_cfg.get("max_per_keyword", 20)),
                days_lookback=arxiv_cfg.get("days_lookback", 3),
            )
        )

    hf_cfg = sources_cfg.get("huggingface", {})
    if hf_cfg.get("enabled", True):
        papers.extend(collect_huggingface(max_papers=hf_cfg.get("max_papers", 100)))

    matched = _attach_taxonomy(papers, taxonomy)
    deduped = _deduplicate(matched)
    LOGGER.info("Collector: %d papers after taxonomy match and dedup", len(deduped))
    return deduped
