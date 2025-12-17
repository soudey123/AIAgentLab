import requests
import feedparser
from urllib.parse import urlencode

ARXIV_API = "https://export.arxiv.org/api/query"

def fetch_arxiv(query: str, max_results: int = 20, start: int = 0):
    """
    Fetch arXiv Atom results reliably.
    Uses requests + explicit User-Agent, then parses XML with feedparser.
    """
    params = {
        # Quoted query helps with multi-word phrases
        "search_query": f'all:"{query}"',
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    url = ARXIV_API + "?" + urlencode(params)

    headers = {
        # arXiv recommends a real UA; some environments get empty/blocked responses otherwise
        "User-Agent": "AegisRAG/1.0 (mailto: you@example.com)"
    }

    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()

    feed = feedparser.parse(r.text)

    docs = []
    for e in getattr(feed, "entries", []):
        text = getattr(e, "summary", "") or getattr(e, "title", "")
        if not text.strip():
            continue
        docs.append({
            "text": text,
            "metadata": {
                "source": "arxiv",
                "title": getattr(e, "title", ""),
                "url": getattr(e, "link", ""),
                "published": getattr(e, "published", "")
            }
        })

    return docs