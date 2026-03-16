"""Rank papers using LLM scoring tailored to auto-research."""

import math

from .taxonomy import get_taxonomy_map
from .utils import get_logger

LOGGER = get_logger(__name__)

RANKING_SYSTEM_PROMPT = (
    "You are curating an awesome repository about Auto-Research / Agentic Research.\n"
    "Score each paper on four dimensions from 1 to 10:\n"
    "1. fit_to_auto_research: relevance to AI systems that assist or automate research\n"
    "2. methodological_significance: how substantial the method contribution is\n"
    "3. ecosystem_relevance: usefulness to builders of research agents, workflows, or tooling\n"
    "4. likely_longevity: chance this work still matters months later\n\n"
    "Known themes: {themes}\n\n"
    'Return JSON: {{ "scores": [ {{ "paper_id": str, "fit_to_auto_research": int, '
    '"methodological_significance": int, "ecosystem_relevance": int, "likely_longevity": int, '
    '"reason": str, "featured": bool }} ] }}\n'
    "Return scores for every paper in the same order and only valid JSON."
)

BATCH_SIZE = 12
DEFAULT_DIMENSIONS = {
    "fit_to_auto_research": 0.35,
    "methodological_significance": 0.3,
    "ecosystem_relevance": 0.2,
    "likely_longevity": 0.15,
}


def _format_papers_for_prompt(papers: list[dict], taxonomy_map: dict[str, dict]) -> str:
    lines = []
    for index, paper in enumerate(papers, 1):
        theme_names = [taxonomy_map[theme]["name"] for theme in paper.get("themes", []) if theme in taxonomy_map]
        lines.append(
            f"[{index}] ID: {paper['paper_id']}\n"
            f"Title: {paper['title']}\n"
            f"Themes: {', '.join(theme_names) if theme_names else 'unclassified'}\n"
            f"Source: {paper['source']}\n"
            f"Abstract: {paper['abstract'][:700]}\n"
        )
    return "\n".join(lines)


def _fallback_scores(papers: list[dict]) -> list[dict]:
    return [
        {
            "paper_id": paper["paper_id"],
            "fit_to_auto_research": 5,
            "methodological_significance": 5,
            "ecosystem_relevance": 5,
            "likely_longevity": 5,
            "reason": "scoring failed",
            "featured": False,
        }
        for paper in papers
    ]


def _score_batch(llm, papers: list[dict], taxonomy: list[dict]) -> list[dict]:
    system = RANKING_SYSTEM_PROMPT.format(
        themes=", ".join(theme["name"] for theme in taxonomy),
    )
    prompt = _format_papers_for_prompt(papers, get_taxonomy_map(taxonomy))
    try:
        result = llm.generate_json(system, prompt, temperature=0.1, max_tokens=4096)
    except Exception as exc:
        LOGGER.error("Ranking LLM call failed: %s", exc)
        return _fallback_scores(papers)

    score_map = {score["paper_id"]: score for score in result.get("scores", [])}
    ordered = []
    for paper in papers:
        ordered.append(score_map.get(paper["paper_id"], _fallback_scores([paper])[0]))
    return ordered


def rank_papers(
    papers: list[dict],
    taxonomy: list[dict],
    llm,
    top_k: int = 25,
    dimensions: dict | None = None,
) -> list[dict]:
    if not papers:
        return []

    dimensions = dimensions or DEFAULT_DIMENSIONS
    all_scores = []
    n_batches = math.ceil(len(papers) / BATCH_SIZE)
    for batch_index in range(n_batches):
        batch = papers[batch_index * BATCH_SIZE:(batch_index + 1) * BATCH_SIZE]
        LOGGER.info("Scoring batch %d/%d (%d papers)", batch_index + 1, n_batches, len(batch))
        all_scores.extend(_score_batch(llm, batch, taxonomy))

    lookup = {score["paper_id"]: score for score in all_scores}
    ranked = []
    for paper in papers:
        score = lookup.get(paper["paper_id"], {})
        composite = sum(float(score.get(name, 5)) * weight for name, weight in dimensions.items())
        enriched = {**paper}
        enriched["scores"] = {
            **{name: score.get(name, 5) for name in DEFAULT_DIMENSIONS},
            "composite": round(composite, 2),
            "reason": score.get("reason", ""),
            "featured": bool(score.get("featured", False)),
        }
        ranked.append(enriched)

    ranked.sort(key=lambda item: item["scores"]["composite"], reverse=True)
    return ranked[:top_k]
