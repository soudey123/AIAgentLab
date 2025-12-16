from typing import List, Optional

from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

from src.prompts import RESEARCH_INSTRUCTIONS, SUMMARY_INSTRUCTIONS
from src.tools import WikipediaSearchTool, FetchPageTextTool, UseProvidedUrlsTool

load_dotenv()


def build_crew(topic: str, urls: Optional[List[str]] = None) -> Crew:
    """
    Build a 2-agent CrewAI pipeline:
      - Researcher: discovers sources (URL mode preferred; search as fallback), fetches pages, extracts evidence
      - Summarizer: produces final sourced brief

    urls: if provided, skips web discovery and uses these URLs as sources.
    """
    gpt52 = LLM(model="gpt-5.2")

    researcher = Agent(
        role="Researcher",
        goal=f"Collect credible sources and evidence for: {topic}",
        backstory="You are great at fast, accurate web research and source tracking.",
        llm=gpt52,
        verbose=True,
        tools=[UseProvidedUrlsTool(), WikipediaSearchTool(), FetchPageTextTool()],
    )

    summarizer = Agent(
        role="Summarizer",
        goal=f"Write a structured, evidence-backed brief for: {topic}",
        backstory="You create crisp, executive-ready briefs from messy notes.",
        llm=gpt52,
        verbose=True,
    )

    urls_block = ""
    if urls:
        # Give the agent URLs directly so it never needs to search.
        urls_block = "\n".join(f"- {u}" for u in urls)

    research_task = Task(
        description=(
            f"{RESEARCH_INSTRUCTIONS}\n\n"
            f"Topic: {topic}\n\n"
            "## Instructions\n"
            "You MUST produce research notes with real URLs under a '## Sources' section.\n\n"
            "### Source discovery rules\n"
            "1) If a URL list is provided below, DO NOT use web_search. Use `use_provided_urls` and treat them as your sources.\n"
            "2) If no URLs are provided, try `web_search` to discover sources.\n"
            "3) For at least 3 sources, call `fetch_page_text` and extract evidence.\n\n"
            "### Provided URLs (if any)\n"
            f"{urls_block if urls_block else '(none)'}\n\n"
            "### Output format (markdown)\n"
            "## Findings\n"
            "- Bullet points with [source](URL)\n"
            "## Notable Quotes (<= 1 sentence each)\n"
            "## Sources\n"
            "- URL list\n"
            "If you cannot access the web (403/blocked), clearly say so and request user-provided URLs.\n"
        ),
        expected_output="Markdown research notes with sources.",
        agent=researcher,
    )

    summary_task = Task(
        description=(
            f"{SUMMARY_INSTRUCTIONS}\n\n"
            f"Topic: {topic}\n"
            "Use ONLY the sources present in the research notes.\n"
            "If the research notes contain no sources, explain what’s missing and how to proceed.\n"
        ),
        expected_output="Final markdown brief with sources.",
        agent=summarizer,
        context=[research_task],
    )

    return Crew(
        agents=[researcher, summarizer],
        tasks=[research_task, summary_task],
        verbose=True,
    )