"""Build structured indexes from archive cards and curated seeds."""

import json
from pathlib import Path

import yaml

from .taxonomy import normalize_theme_id


def _load_curated(data_dir: Path) -> dict:
    curated_path = data_dir / "curated.yaml"
    if not curated_path.exists():
        return {"repos": [], "landmark_papers": []}
    with open(curated_path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {"repos": [], "landmark_papers": []}


def _load_archive_metadata(project_dir: Path, archive_dir_name: str) -> list[dict]:
    metadata_path = project_dir / archive_dir_name / "metadata.json"
    if not metadata_path.exists():
        return []
    return json.loads(metadata_path.read_text(encoding="utf-8"))


def _taxonomy_index(taxonomy: list[dict]) -> list[dict]:
    indexed = []
    for theme in taxonomy:
        indexed.append({
            "id": normalize_theme_id(theme["id"]),
            "name": theme["name"],
            "query_keywords": theme.get("query_keywords", []),
            "exclude_keywords": theme.get("exclude_keywords", []),
            "repo_tags": theme.get("repo_tags", []),
            "readme_section": theme.get("readme_section", "Key Papers by Theme"),
        })
    return indexed


def sync_indexes(project_dir: Path, cfg: dict, archived_papers: list[dict] | None = None) -> dict:
    output_cfg = cfg.get("output", {})
    data_dir = project_dir / output_cfg.get("data_dir", "data")
    data_dir.mkdir(parents=True, exist_ok=True)
    archive_dir_name = output_cfg.get("archive_dir", "archive")

    curated = _load_curated(data_dir)
    papers = _load_archive_metadata(project_dir, archive_dir_name)
    repos = curated.get("repos", [])
    taxonomy = _taxonomy_index(cfg.get("taxonomy", []))

    (data_dir / "papers.json").write_text(json.dumps(papers, indent=2, ensure_ascii=False), encoding="utf-8")
    (data_dir / "repos.json").write_text(json.dumps(repos, indent=2, ensure_ascii=False), encoding="utf-8")
    (data_dir / "taxonomy.json").write_text(json.dumps(taxonomy, indent=2, ensure_ascii=False), encoding="utf-8")
    return {"papers": papers, "repos": repos, "taxonomy": taxonomy}
