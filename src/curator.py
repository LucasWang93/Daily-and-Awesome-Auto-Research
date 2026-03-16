"""Render semi-automated README sections from curated data and archived papers."""

import json
from collections import defaultdict
from pathlib import Path

import yaml

from .taxonomy import normalize_theme_id

README_TEMPLATE = """# Awesome Auto-Research

An English-first curated knowledge base for autoresearch loops, AI scientist systems, automated discovery frameworks, and research-agent infrastructure.

## What Is Auto-Research?

This repository follows the spirit of `karpathy/autoresearch`: agents run tight research loops, modify code or plans, measure outcomes, keep what works, and accumulate progress. From that baseline, we also track broader AI scientist systems, closed-loop empirical science frameworks, and infrastructure that makes continual machine-driven research possible.

## Most Important GitHub Repos

<!-- BEGIN: curated-repos -->
<!-- END: curated-repos -->

## Key Papers By Theme

<!-- BEGIN: theme-papers -->
<!-- END: theme-papers -->

## Recent Additions

<!-- BEGIN: recent-papers -->
<!-- END: recent-papers -->

## Featured This Week

<!-- BEGIN: featured-papers -->
<!-- END: featured-papers -->

## Latest Archive Entry

<!-- BEGIN: latest-entry -->
<!-- END: latest-entry -->
"""


def _load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _load_curated(data_dir: Path) -> dict:
    curated_path = data_dir / "curated.yaml"
    if not curated_path.exists():
        return {"repos": [], "landmark_papers": []}
    with open(curated_path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {"repos": [], "landmark_papers": []}


def _replace_block(content: str, marker: str, block: str) -> str:
    begin = f"<!-- BEGIN: {marker} -->"
    end = f"<!-- END: {marker} -->"
    start = content.index(begin) + len(begin)
    finish = content.index(end)
    return content[:start] + "\n" + block.rstrip() + "\n" + content[finish:]


def _render_repos(repos: list[dict]) -> str:
    required = {"name", "url", "positioning", "why_it_matters", "relation", "representative", "status"}
    category_titles = {
        "reference_loop": "### Reference Loop",
        "end_to_end_ai_scientists": "### End-to-End AI Scientist Systems",
        "closed_loop_science": "### Closed-Loop Science Frameworks",
        "literature_and_review_agents": "### Literature And Review Agents",
        "infrastructure_and_tools": "### Infrastructure And Tools",
    }
    grouped = defaultdict(list)
    for repo in repos:
        missing = sorted(required - repo.keys())
        if missing:
            raise ValueError(f"Curated repo '{repo.get('name', 'unknown')}' missing fields: {', '.join(missing)}")
        category = repo.get("category", "infrastructure_and_tools")
        grouped[category].append(
            f"- [{repo['name']}]({repo['url']}) [{repo['status']}]: {repo['positioning']}. "
            f"Why it matters: {repo['why_it_matters']} Relation to auto-research: {repo['relation']} "
            f"Representative reference: {repo['representative']}."
        )
    if not grouped:
        return "- Curated repos will appear here."

    lines = []
    for category in category_titles:
        items = grouped.get(category, [])
        if not items:
            continue
        lines.append(category_titles[category])
        lines.extend(items)
        lines.append("")
    return "\n".join(lines).strip()


def _render_theme_papers(taxonomy: list[dict], landmark_papers: list[dict]) -> str:
    grouped = defaultdict(list)
    for paper in landmark_papers:
        for theme_id in paper.get("themes", []):
            grouped[normalize_theme_id(theme_id)].append(paper)

    lines = []
    for theme in taxonomy:
        norm_id = normalize_theme_id(theme["id"])
        lines.append(f"### {theme['name']}")
        items = grouped.get(norm_id, [])
        if not items:
            lines.append("- No landmark papers added yet.")
            lines.append("")
            continue
        for paper in items:
            lines.append(f"- [{paper['title']}]({paper['url']}): {paper['summary']}")
        lines.append("")
    return "\n".join(lines).strip()


def _render_recent(papers: list[dict], limit: int) -> str:
    if not papers:
        return "- No archived additions yet."
    lines = []
    for paper in papers[:limit]:
        archive_path = paper.get("archive_path", "")
        lines.append(
            f"- **{paper['date']}** [{paper['title']}]({paper['links'].get('paper', '')})"
            f" ({', '.join(paper.get('theme_names', paper.get('themes', [])))})"
            f" - card: [{Path(archive_path).name}]({archive_path})"
        )
    return "\n".join(lines)


def _render_featured(papers: list[dict], limit: int) -> str:
    featured = [paper for paper in papers if paper.get("featured")]
    if not featured:
        return "- No featured papers yet."
    lines = []
    for paper in featured[:limit]:
        lines.append(
            f"- [{paper['title']}]({paper['links'].get('paper', '')}): {paper.get('why_it_matters', paper.get('reason', ''))}"
        )
    return "\n".join(lines)


def _render_latest_entry(papers: list[dict]) -> str:
    if not papers:
        return "No archive entries yet."
    latest = papers[0]
    return (
        f"[{latest['title']}]({latest['links'].get('paper', '')})"
        f" is the latest archived addition. Themes: {', '.join(latest.get('theme_names', latest.get('themes', [])))}. "
        f"Why it matters: {latest.get('why_it_matters', latest.get('reason', ''))}"
    )


def build_readme(project_dir: Path, cfg: dict) -> Path:
    output_cfg = cfg.get("output", {})
    data_dir = project_dir / output_cfg.get("data_dir", "data")
    readme_path = project_dir / "README.md"
    if not readme_path.exists():
        readme_path.write_text(README_TEMPLATE, encoding="utf-8")

    content = readme_path.read_text(encoding="utf-8")
    if "<!-- BEGIN: curated-repos -->" not in content:
        content = README_TEMPLATE

    curated = _load_curated(data_dir)
    papers = _load_json(data_dir / "papers.json", [])
    recent_limit = cfg.get("readme", {}).get("recent_limit", 10)
    featured_limit = cfg.get("readme", {}).get("featured_limit", 5)
    papers = sorted(papers, key=lambda item: (item.get("date", ""), item.get("importance_score", 0)), reverse=True)

    content = _replace_block(content, "curated-repos", _render_repos(curated.get("repos", [])))
    content = _replace_block(
        content,
        "theme-papers",
        _render_theme_papers(cfg.get("taxonomy", []), curated.get("landmark_papers", [])),
    )
    content = _replace_block(content, "recent-papers", _render_recent(papers, recent_limit))
    content = _replace_block(content, "featured-papers", _render_featured(papers, featured_limit))
    content = _replace_block(content, "latest-entry", _render_latest_entry(papers))

    readme_path.write_text(content, encoding="utf-8")
    return readme_path
