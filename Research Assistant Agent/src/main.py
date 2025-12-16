from pathlib import Path
import sys
from typing import List

from dotenv import load_dotenv

from src.crew import build_crew
from src.tools import write_file


# Always load .env from project root (reliable in VS Code / Replit)
ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")


def run(topic: str, urls: List[str] | None = None):
    crew = build_crew(topic, urls=urls)
    result = crew.kickoff()
    path = write_file("output/report.md", str(result))
    print(f"\n✅ Report saved to: {path}\n")


if __name__ == "__main__":
    # Default topic
    topic = "Competitive analysis: AI agent platforms for research + summarization"

    # Optional CLI:
    #   python -m src.main "my topic" url1 url2 url3
    if len(sys.argv) >= 2:
        topic = sys.argv[1]

    urls = None
    if len(sys.argv) > 2:
        urls = sys.argv[2:]  # any extra args treated as URLs

    # ✅ Recommended: hardcode a starter set of URLs if none provided
    if urls is None:
        urls = [
            "https://docs.crewai.com/",
            "https://python.langchain.com/docs/langgraph/",
            "https://docs.llamaindex.ai/",
        ]

    run(topic, urls=urls)