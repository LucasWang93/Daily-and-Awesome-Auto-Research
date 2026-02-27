"""Rank papers using GPT-5 on relevance, novelty, and impact."""

import math

from .llm import LLMClient
from .utils import get_logger

LOGGER = get_logger(__name__)

RANKING_SYSTEM_PROMPT = (
    "You are a senior AI researcher. You will receive a batch of academic paper "
    "titles and abstracts. For each paper, score it on three dimensions (1-10 scale):\n\n"
    "1. relevance: How relevant is this paper to the given research topics?\n"
    "2. novelty: How novel is the approach, method, or finding?\n"
    "3. impact: How impactful could this work be for the field?\n\n"
    "Research topics of interest: {topics}\n\n"
    'Return a JSON object with key "scores" containing an array. Each element must have:\n'
    '- "paper_id": the paper ID (string)\n'
    '- "relevance": integer 1-10\n'
    '- "novelty": integer 1-10\n'
    '- "impact": integer 1-10\n'
    '- "reason": a brief sentence explaining the score\n\n'
    "IMPORTANT: Return scores for ALL papers in the input, in the same order.\n"
    "Return ONLY valid JSON. No markdown fences."
)

BATCH_SIZE = 15


def _format_papers_for_prompt(papers: list[dict]) -> str:
    lines = []
    for i, p in enumerate(papers, 1):
        lines.append(
            f"[{i}] ID: {p['paper_id']}\n"
            f"    Title: {p['title']}\n"
            f"    Abstract: {p['abstract'][:500]}\n"
            f"    Source: {p['source']}\n"
            f"    Keywords matched: {', '.join(p.get('keywords_matched', []))}\n"
        )
    return "\n".join(lines)


def _score_batch(
    llm: LLMClient,
    papers: list[dict],
    topics: list[str],
) -> list[dict]:
    """Score a batch of papers via a single LLM call."""
    system = RANKING_SYSTEM_PROMPT.format(topics=", ".join(topics))
    user = _format_papers_for_prompt(papers)

    try:
        result = llm.generate_json(system, user, temperature=0.1, max_tokens=4096)
    except Exception as exc:
        LOGGER.error("Ranking LLM call failed: %s", exc)
        return [
            {"paper_id": p["paper_id"], "relevance": 5, "novelty": 5,
             "impact": 5, "reason": "scoring failed"}
            for p in papers
        ]

    scores = result.get("scores", [])
    score_map = {s["paper_id"]: s for s in scores}

    ordered = []
    for p in papers:
        pid = p["paper_id"]
        if pid in score_map:
            ordered.append(score_map[pid])
        else:
            ordered.append({
                "paper_id": pid, "relevance": 5, "novelty": 5,
                "impact": 5, "reason": "not returned by LLM",
            })
    return ordered


def rank_papers(
    papers: list[dict],
    topics: list[str],
    llm: LLMClient,
    top_k: int = 20,
) -> list[dict]:
    """Score and rank all papers, return top-k with scores attached."""
    if not papers:
        LOGGER.warning("No papers to rank")
        return []

    all_scores: list[dict] = []
    n_batches = math.ceil(len(papers) / BATCH_SIZE)

    for batch_idx in range(n_batches):
        start = batch_idx * BATCH_SIZE
        end = start + BATCH_SIZE
        batch = papers[start:end]
        LOGGER.info(
            "Scoring batch %d/%d (%d papers)",
            batch_idx + 1, n_batches, len(batch),
        )
        scores = _score_batch(llm, batch, topics)
        all_scores.extend(scores)

    score_lookup = {s["paper_id"]: s for s in all_scores}

    scored_papers = []
    for p in papers:
        s = score_lookup.get(p["paper_id"], {})
        rel = s.get("relevance", 5)
        nov = s.get("novelty", 5)
        imp = s.get("impact", 5)
        composite = rel * 0.4 + nov * 0.3 + imp * 0.3

        enriched = {**p}
        enriched["scores"] = {
            "relevance": rel,
            "novelty": nov,
            "impact": imp,
            "composite": round(composite, 2),
            "reason": s.get("reason", ""),
        }
        scored_papers.append(enriched)

    scored_papers.sort(key=lambda x: x["scores"]["composite"], reverse=True)
    top = scored_papers[:top_k]

    LOGGER.info(
        "Ranking complete: %d papers scored, top-%d selected (best=%.2f, cutoff=%.2f)",
        len(scored_papers), len(top),
        top[0]["scores"]["composite"] if top else 0,
        top[-1]["scores"]["composite"] if top else 0,
    )
    return top
