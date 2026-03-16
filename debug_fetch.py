#!/usr/bin/env python3
"""Minimal network probe for arXiv / Hugging Face sources."""

from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def probe(name: str, url: str) -> None:
    print(f"=== {name} ===")
    req = Request(url, headers={"User-Agent": "AwesomeAutoResearch/1.0 (diagnostic)"})
    try:
        with urlopen(req, timeout=30) as resp:
            print("STATUS", resp.status)
            print("HEADERS")
            for key, value in resp.headers.items():
                print(f"{key}: {value}")
            body = resp.read(400).decode("utf-8", errors="replace")
            print("BODY", body)
    except HTTPError as exc:
        print("HTTP_ERROR", exc.code)
        print("HEADERS")
        for key, value in exc.headers.items():
            print(f"{key}: {value}")
        try:
            print("BODY", exc.read(400).decode("utf-8", errors="replace"))
        except Exception as inner_exc:
            print("BODY_READ_FAILED", repr(inner_exc))
    except URLError as exc:
        print("URL_ERROR", repr(exc))
    except Exception as exc:
        print("OTHER_ERROR", type(exc).__name__, repr(exc))
    print()


def main() -> None:
    probe(
        "arXiv autodiscovery query",
        "https://export.arxiv.org/api/query?search_query=all%3A%22autodiscovery%22&start=0&max_results=5&sortBy=submittedDate&sortOrder=descending",
    )
    probe("HuggingFace daily papers", "https://huggingface.co/api/daily_papers")


if __name__ == "__main__":
    main()
