import os
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


# ---------------------------
# Low-level helper functions
# ---------------------------
def _wikipedia_search(query: str, k: int = 6) -> List[Dict]:
    """
    Wikipedia search API (stable, no scraping, no API key).
    NOTE: Some corporate networks block this endpoint (403). If so, use URL mode.
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": k,
        "origin": "*",  # can help in some locked-down environments
    }
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        ),
        "Accept": "application/json,text/plain,*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://en.wikipedia.org/",
    }

    r = requests.get(url, params=params, headers=headers, timeout=30)
    r.raise_for_status()
    data = r.json()

    results: List[Dict] = []
    for item in data.get("query", {}).get("search", []):
        title = item.get("title", "")
        page_url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
        results.append(
            {
                "title": title,
                "link": page_url,
                "snippet": item.get("snippet", ""),
            }
        )
    return results


def _fetch_page_text(url: str, max_chars: int = 8000) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    # Remove noise
    for tag in soup(["script", "style", "noscript", "table"]):
        tag.decompose()

    text = " ".join(soup.get_text(" ").split())
    return text[:max_chars]


def write_file(path: str, content: str) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


# ---------------------------
# CrewAI Tool wrappers
# ---------------------------
class SearchInput(BaseModel):
    query: str = Field(..., description="Search query")
    k: int = Field(6, description="Number of results to return")


class WikipediaSearchTool(BaseTool):
    name: str = "web_search"
    description: str = (
        "Search Wikipedia for relevant pages and return titles and URLs. "
        "If blocked (403), use provided URLs instead."
    )
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str, k: int = 6) -> str:
        results = _wikipedia_search(query=query, k=k)
        if not results:
            return "No Wikipedia results found."
        return "\n".join(f"- {r['title']} ({r['link']})" for r in results)


# ✅ NEW: URL-mode tool (fixes your ImportError)
class UrlListInput(BaseModel):
    urls: List[str] = Field(..., description="List of URLs to analyze (3-10 recommended)")


class UseProvidedUrlsTool(BaseTool):
    name: str = "use_provided_urls"
    description: str = "Use user-provided URLs as the source list (no web search)."
    args_schema: Type[BaseModel] = UrlListInput

    def _run(self, urls: List[str]) -> str:
        cleaned = [u.strip() for u in urls if u and u.strip()]
        if not cleaned:
            return "No URLs provided."
        return "\n".join(f"- {u}" for u in cleaned)


class FetchPageInput(BaseModel):
    url: str = Field(..., description="URL of the webpage to fetch")
    max_chars: int = Field(8000, description="Max characters to return")


class FetchPageTextTool(BaseTool):
    name: str = "fetch_page_text"
    description: str = "Fetch a webpage and extract readable text."
    args_schema: Type[BaseModel] = FetchPageInput

    def _run(self, url: str, max_chars: int = 8000) -> str:
        return _fetch_page_text(url=url, max_chars=max_chars)