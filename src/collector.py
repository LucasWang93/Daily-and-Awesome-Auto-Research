"""Collect papers from ArXiv, Nature journals, and HuggingFace Daily Papers."""

import json
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from typing import Optional
from urllib.error import URLError
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

import feedparser

from .utils import get_logger

LOGGER = get_logger(__name__)

ARXIV_API_URL = "https://export.arxiv.org/api/query"
HF_DAILY_URL = "https://huggingface.co/api/daily_papers"
NATURE_RSS_TEMPLATE = "https://www.nature.com/{journal}.rss"
NATURE_SEARCH_URL = "https://www.nature.com/search"


def _http_get(url: str, retries: int = 3, timeout: int = 30) -> Optional[str]:
    for attempt in range(retries):
        try:
            req = Request(url, headers={
                "User-Agent": "DailyPapersAssistant/1.0 (academic research tool)",
            })
            with urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8")
        except (URLError, TimeoutError, OSError) as exc:
            LOGGER.warning("HTTP GET %s attempt %d failed: %s", url, attempt + 1, exc)
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    return None


_KEYWORD_EXPANSIONS = {
    "multi-modal llm": ["multimodal", "multi-modal", "vision-language", "vision language",
                        "vlm", "mllm", "gpt-4v", "gpt-4o", "gemini", "omni-modal"],
    "vla": ["vision-language-action", "vision language action", "robot manipulation",
            "embodied ai", "robotic policy"],
    "llm agents": ["llm agent", "language model agent", "tool-use", "tool use",
                   "agentic", "autonomous agent", "ai agent"],
    "agentic rl": ["agentic reinforcement", "agent reinforcement learning",
                   "rl agent", "reward shaping agent", "policy optimization agent"],
    "medical agents": ["medical ai", "clinical agent", "health agent",
                       "biomedical agent", "medical llm", "clinical llm"],
}


def _matches_keywords(text: str, keywords: list[str]) -> list[str]:
    """Return keywords matching text, using expanded synonyms for broader recall."""
    text_lower = text.lower()
    matched = []
    for kw in keywords:
        if kw.lower() in text_lower:
            matched.append(kw)
            continue
        expansions = _KEYWORD_EXPANSIONS.get(kw.lower(), [])
        if any(syn in text_lower for syn in expansions):
            matched.append(kw)
    return matched


# ---------------------------------------------------------------------------
# ArXiv
# ---------------------------------------------------------------------------

def collect_arxiv(
    keywords: list[str],
    max_per_keyword: int = 30,
    days_lookback: int = 2,
) -> list[dict]:
    """Search ArXiv for recent papers matching each keyword."""
    papers: list[dict] = []

    for kw in keywords:
        query = quote_plus(f'all:"{kw}"')
        url = (
            f"{ARXIV_API_URL}?search_query={query}"
            f"&start=0&max_results={max_per_keyword}"
            f"&sortBy=submittedDate&sortOrder=descending"
        )
        raw = _http_get(url)
        if not raw:
            LOGGER.warning("ArXiv query failed for keyword: %s", kw)
            continue

        try:
            root = ET.fromstring(raw)
        except ET.ParseError:
            LOGGER.error("ArXiv XML parse error for keyword: %s", kw)
            continue

        ns = {"atom": "http://www.w3.org/2005/Atom"}
        cutoff = datetime.now(timezone.utc) - timedelta(days=days_lookback)

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

            arxiv_id = ""
            id_el = entry.find("atom:id", ns)
            if id_el is not None and id_el.text:
                m = re.search(r"abs/(.+)$", id_el.text)
                arxiv_id = m.group(1) if m else id_el.text

            title_el = entry.find("atom:title", ns)
            title = (title_el.text or "").strip().replace("\n", " ") if title_el is not None else ""

            summary_el = entry.find("atom:summary", ns)
            abstract = (summary_el.text or "").strip().replace("\n", " ") if summary_el is not None else ""

            authors = [
                a.find("atom:name", ns).text
                for a in entry.findall("atom:author", ns)
                if a.find("atom:name", ns) is not None and a.find("atom:name", ns).text
            ]

            if not arxiv_id or not title:
                continue

            matched = _matches_keywords(f"{title} {abstract}", keywords)

            papers.append({
                "paper_id": arxiv_id,
                "title": title,
                "abstract": abstract,
                "authors": authors,
                "url": f"https://arxiv.org/abs/{arxiv_id}",
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "date": pub_date.strftime("%Y-%m-%d"),
                "source": "arxiv",
                "keywords_matched": matched or [kw],
            })

        time.sleep(1)

    LOGGER.info("ArXiv: collected %d raw entries across %d keywords", len(papers), len(keywords))
    return papers


# ---------------------------------------------------------------------------
# HuggingFace Daily Papers
# ---------------------------------------------------------------------------

def collect_huggingface(
    keywords: list[str],
    max_papers: int = 100,
) -> list[dict]:
    """Fetch HuggingFace daily papers and filter by keywords."""
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
        title = paper.get("title", "")
        abstract = paper.get("summary", paper.get("abstract", ""))
        paper_id = paper.get("id", "")

        if not paper_id or not title:
            continue

        matched = _matches_keywords(f"{title} {abstract}", keywords)
        if not matched:
            continue

        authors = [
            a.get("name", a) if isinstance(a, dict) else str(a)
            for a in paper.get("authors", [])
        ]

        papers.append({
            "paper_id": paper_id,
            "title": title.strip(),
            "abstract": abstract.strip(),
            "authors": authors,
            "url": f"https://arxiv.org/abs/{paper_id}",
            "pdf_url": f"https://arxiv.org/pdf/{paper_id}",
            "date": paper.get("publishedAt", paper.get("published", ""))[:10],
            "source": "huggingface_daily",
            "keywords_matched": matched,
        })

    LOGGER.info("HuggingFace Daily: %d papers matched keywords out of %d total", len(papers), len(items))
    return papers


# ---------------------------------------------------------------------------
# Nature journals (RSS feeds)
# ---------------------------------------------------------------------------

def collect_nature(
    keywords: list[str],
    journals: list[str] | None = None,
) -> list[dict]:
    """Fetch recent papers from Nature journal RSS feeds, filter by keywords."""
    if journals is None:
        journals = ["nature", "natmachintell", "natmed", "natbiomedeng", "natcomms"]

    papers: list[dict] = []

    for journal in journals:
        feed_url = NATURE_RSS_TEMPLATE.format(journal=journal)
        LOGGER.info("Fetching Nature RSS: %s", feed_url)
        raw = _http_get(feed_url, timeout=20)
        if not raw:
            LOGGER.warning("Failed to fetch RSS for %s", journal)
            continue

        feed = feedparser.parse(raw)
        for entry in feed.entries:
            title = entry.get("title", "")
            abstract = entry.get("summary", entry.get("description", ""))
            link = entry.get("link", "")

            if not title:
                continue

            matched = _matches_keywords(f"{title} {abstract}", keywords)
            if not matched:
                continue

            pub_date = ""
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                pub_date = time.strftime("%Y-%m-%d", entry.published_parsed)

            doi = entry.get("prism_doi", entry.get("dc_identifier", ""))
            paper_id = doi or link

            authors = []
            if hasattr(entry, "authors"):
                authors = [a.get("name", "") for a in entry.authors if a.get("name")]
            elif hasattr(entry, "author"):
                authors = [entry.author]

            papers.append({
                "paper_id": paper_id,
                "title": title.strip(),
                "abstract": abstract.strip(),
                "authors": authors,
                "url": link,
                "pdf_url": "",
                "date": pub_date,
                "source": f"nature_{journal}",
                "keywords_matched": matched,
            })

        time.sleep(0.5)

    LOGGER.info("Nature RSS: %d papers matched keywords across %d journals", len(papers), len(journals))
    return papers


# ---------------------------------------------------------------------------
# Unified collection + deduplication
# ---------------------------------------------------------------------------

def _deduplicate(papers: list[dict]) -> list[dict]:
    """Remove duplicate papers by paper_id, keeping the first occurrence."""
    seen: set[str] = set()
    result: list[dict] = []
    for p in papers:
        pid = p["paper_id"]
        if pid and pid not in seen:
            seen.add(pid)
            result.append(p)
    return result


def collect_all(
    keywords: list[str],
    arxiv_cfg: dict | None = None,
    nature_cfg: dict | None = None,
    hf_cfg: dict | None = None,
) -> list[dict]:
    """Run all collectors and return deduplicated paper list."""
    arxiv_cfg = arxiv_cfg or {}
    nature_cfg = nature_cfg or {}
    hf_cfg = hf_cfg or {}

    all_papers: list[dict] = []

    if arxiv_cfg.get("enabled", True):
        all_papers.extend(collect_arxiv(
            keywords,
            max_per_keyword=arxiv_cfg.get("max_per_keyword", 30),
            days_lookback=arxiv_cfg.get("days_lookback", 2),
        ))

    if hf_cfg.get("enabled", True):
        all_papers.extend(collect_huggingface(
            keywords,
            max_papers=hf_cfg.get("max_papers", 100),
        ))

    if nature_cfg.get("enabled", True):
        all_papers.extend(collect_nature(
            keywords,
            journals=nature_cfg.get("journals"),
        ))

    deduped = _deduplicate(all_papers)
    LOGGER.info(
        "Collection complete: %d total -> %d after dedup",
        len(all_papers), len(deduped),
    )
    return deduped
