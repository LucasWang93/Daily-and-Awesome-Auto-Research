"""Taxonomy helpers for agentic research themes."""

import re


def normalize_theme_id(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def get_taxonomy_map(taxonomy: list[dict]) -> dict[str, dict]:
    return {normalize_theme_id(theme["id"]): {**theme, "id": normalize_theme_id(theme["id"])} for theme in taxonomy}


def collect_query_terms(taxonomy: list[dict]) -> list[str]:
    seen = set()
    terms = []
    for theme in taxonomy:
        for keyword in theme.get("query_keywords", []):
            lowered = keyword.lower().strip()
            if lowered and lowered not in seen:
                seen.add(lowered)
                terms.append(keyword)
    return terms


def find_theme_matches(text: str, taxonomy: list[dict]) -> list[dict]:
    text_lower = text.lower()
    matches = []
    for theme in taxonomy:
        keywords = [kw.lower() for kw in theme.get("query_keywords", [])]
        exclusions = [kw.lower() for kw in theme.get("exclude_keywords", [])]
        if exclusions and any(keyword in text_lower for keyword in exclusions):
            continue
        if any(keyword in text_lower for keyword in keywords):
            matches.append({**theme, "id": normalize_theme_id(theme["id"])})
    return matches
