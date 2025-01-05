from crewai import Agent
from src.tools import ResearchTools

def create_agents():
    agents = {
        "profile_manager": Agent(
            role="Profile Manager",
            goal="Understand user interests and maintain user profiles.",
            backstory="Expert in academic interests and research preferences.",
            verbose=True,
            allow_delegation=False,
            tools=[]
        ),
        "article_retriever": Agent(
            role="Article Retriever",
            goal="Find relevant articles matching user interests and disciplines, rank by citations, and filter by preferred journals.",
            backstory="Expert in finding academic articles and tailoring results.",
            verbose=True,
            allow_delegation=False,
            tools=[
                ResearchTools.search_google_scholar
            ]
        ),
        "content_analyzer": Agent(
            role="Content Analyzer",
            goal="Analyze articles for relevance and generate personalized recommendations.",
            backstory="Expert in academic content analysis and GPT-enhanced recommendations.",
            verbose=True,
            allow_delegation=True,
            tools=[
                ResearchTools.enhance_with_gpt
            ]
        ),
    }

    return agents