from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

from src.prompts import RESEARCH_INSTRUCTIONS, SUMMARY_INSTRUCTIONS
from src.tools import WikipediaSearchTool, FetchPageTextTool

load_dotenv()

def build_crew(topic: str) -> Crew:
    gpt52 = LLM(model="gpt-5.2")

    researcher = Agent(
        role="Researcher",
        goal=f"Research the topic: {topic} and collect credible sources with evidence.",
        backstory="You are great at fast, accurate web research and source tracking.",
        llm=gpt52,
        verbose=True,
        #tools=[DuckDuckGoSearchTool(), FetchPageTextTool()]
        tools=[WikipediaSearchTool(), FetchPageTextTool()],  # ✅ proper tools
    )

    summarizer = Agent(
        role="Summarizer",
        goal=f"Summarize research into a structured brief for: {topic}",
        backstory="You create crisp, executive-ready briefs from messy notes.",
        llm=gpt52,
        verbose=True,
    )

    research_task = Task(
        description=(
            f"{RESEARCH_INSTRUCTIONS}\n\n"
            f"Topic: {topic}\n"
            "1) Use `web_search` to find 6 relevant results.\n"
            "2) Use `fetch_page_text` on at least 3 top URLs.\n"
            "3) Extract evidence and include sources.\n"
        ),
        expected_output="Markdown research notes with sources.",
        agent=researcher,
    )

    summary_task = Task(
        description=(
            f"{SUMMARY_INSTRUCTIONS}\n\n"
            f"Topic: {topic}\n"
            "Use ONLY the sources present in the research notes.\n"
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