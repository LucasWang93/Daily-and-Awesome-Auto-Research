import tempfile
import unittest
from pathlib import Path
import json

import yaml

from src.curator import README_TEMPLATE, build_readme
from src.indexer import sync_indexes
from src.summarizer import generate_report


class CuratorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.project_dir = Path(self.tmp.name)
        (self.project_dir / "archive").mkdir()
        (self.project_dir / "data").mkdir()
        (self.project_dir / "README.md").write_text(README_TEMPLATE, encoding="utf-8")
        (self.project_dir / "archive" / "metadata.json").write_text(
            """[
              {
                "id": "2401.00001",
                "paper_id": "2401.00001",
                "title": "Auto Research Agents",
                "date": "2026-03-16",
                "theme_names": ["Agentic Research"],
                "themes": ["agentic_research"],
                "importance_score": 8.9,
                "reason": "important",
                "why_it_matters": "Shows a strong end-to-end research workflow.",
                "digest_summary": "This paper presents a readable end-to-end workflow for automating parts of research.",
                "summary_short": ["Readable workflow", "End-to-end automation", "Research agent focus"],
                "featured": true,
                "links": {"paper": "https://arxiv.org/abs/2401.00001"},
                "archive_path": "archive/papers/2026-03-16/auto-research-agents.md"
              }
            ]""",
            encoding="utf-8",
        )
        curated = {
            "repos": [
                {
                    "name": "The AI Scientist",
                    "url": "https://github.com/SakanaAI/AI-Scientist",
                    "positioning": "Automated research loop",
                    "why_it_matters": "Landmark repo",
                    "relation": "Defines the end-to-end target",
                    "representative": "The AI Scientist paper",
                    "status": "landmark",
                }
            ],
            "landmark_papers": [
                {
                    "title": "The AI Scientist",
                    "url": "https://arxiv.org/abs/2408.06292",
                    "summary": "Reference system",
                    "themes": ["ai_scientist"],
                }
            ],
        }
        with open(self.project_dir / "data" / "curated.yaml", "w", encoding="utf-8") as f:
            yaml.safe_dump(curated, f, sort_keys=False)
        self.cfg = {
            "taxonomy": [
                {"id": "agentic_research", "name": "Agentic Research"},
                {"id": "ai_scientist", "name": "AI Scientist"},
            ],
            "output": {"archive_dir": "archive", "data_dir": "data"},
            "readme": {"recent_limit": 10, "featured_limit": 5},
        }

    def tearDown(self):
        self.tmp.cleanup()

    def test_sync_and_build_readme(self):
        sync_indexes(self.project_dir, self.cfg)
        readme_path = build_readme(self.project_dir, self.cfg)
        content = readme_path.read_text(encoding="utf-8")
        self.assertIn("The AI Scientist", content)
        self.assertIn("Auto Research Agents", content)
        self.assertIn("latest archived addition", content.lower())

    def test_sync_indexes_uses_full_archive_metadata(self):
        sync_indexes(
            self.project_dir,
            self.cfg,
            archived_papers=[{"id": "should-not-win", "title": "Transient"}],
        )
        papers = json.loads((self.project_dir / "data" / "papers.json").read_text(encoding="utf-8"))
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]["id"], "2401.00001")

    def test_generate_report_uses_digest_summary(self):
        paper = json.loads((self.project_dir / "archive" / "metadata.json").read_text(encoding="utf-8"))[0]
        report_path = generate_report([], None, self.project_dir / "reports", archived_summaries=[paper])
        content = report_path.read_text(encoding="utf-8")
        self.assertIn("## Today in Auto-Research", content)
        self.assertIn("## Top Papers Today", content)
        self.assertIn("readable end-to-end workflow", content.lower())


if __name__ == "__main__":
    unittest.main()
