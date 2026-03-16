import unittest
from urllib.error import HTTPError

from src.collector import _compute_retry_delay, _deduplicate
from src.taxonomy import find_theme_matches


class TaxonomyTests(unittest.TestCase):
    def test_find_theme_matches(self):
        taxonomy = [
            {"id": "agentic_research", "query_keywords": ["research agent"], "exclude_keywords": []},
            {"id": "ai_scientist", "query_keywords": ["AI scientist"], "exclude_keywords": []},
        ]
        matches = find_theme_matches("This paper studies an AI scientist research agent.", taxonomy)
        self.assertEqual([match["id"] for match in matches], ["agentic_research", "ai_scientist"])

    def test_deduplicate_prefers_arxiv_source(self):
        papers = [
            {
                "paper_id": "1234.5678",
                "source": "huggingface_daily",
                "url": "https://huggingface.co/papers/1234.5678",
                "pdf_url": "https://arxiv.org/pdf/1234.5678",
                "themes": ["agentic_research"],
                "theme_names": ["Agentic Research"],
                "links": {"paper": "https://huggingface.co/papers/1234.5678"},
            },
            {
                "paper_id": "1234.5678",
                "source": "arxiv",
                "url": "https://arxiv.org/abs/1234.5678",
                "pdf_url": "https://arxiv.org/pdf/1234.5678",
                "themes": ["ai_scientist"],
                "theme_names": ["AI Scientist"],
                "links": {"paper": "https://arxiv.org/abs/1234.5678"},
            },
        ]
        merged = _deduplicate(papers)
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["source"], "arxiv")
        self.assertEqual(sorted(merged[0]["themes"]), ["agentic_research", "ai_scientist"])

    def test_retry_delay_for_arxiv_rate_limit_is_longer(self):
        exc = HTTPError("https://export.arxiv.org/api/query", 429, "rate limited", hdrs=None, fp=None)
        self.assertEqual(_compute_retry_delay(exc, 1), 15.0)
        self.assertEqual(_compute_retry_delay(exc, 2), 30.0)


if __name__ == "__main__":
    unittest.main()
