from serpapi import GoogleSearch
from typing import List, Optional
from datetime import datetime
from .data_models import Article
import openai

class ResearchTools:
    @staticmethod
    def search_google_scholar(query: str, start_date: datetime, end_date: datetime, max_results: int = 20) -> List[Article]:
        """
        Fetch articles from Google Scholar using SERPAPI with citation numbers included.
        """
        api_key = "76a4acf1ebbb53f041a35664d654017acc1b8d42482ea42eaf816df09b3b0f7b"  # Replace with your SERPAPI key
        params = {
            "engine": "google_scholar",
            "q": query,
            "as_ylo": start_date.year,
            "as_yhi": end_date.year,
            "hl": "en",
            "num": max_results,
            "api_key": api_key,
        }

        try:
            search = GoogleSearch(params)
            results = search.get_dict()

            articles = []
            for result in results.get("organic_results", []):
                try:
                    publication_info = result.get("publication_info", {})
                    publication_date = ResearchTools.parse_publication_date(publication_info.get("summary", ""))
                    citations = result.get("inline_links", {}).get("cited_by", {}).get("total", 0)

                    articles.append(Article(
                        title=result.get("title", "No title available"),
                        authors=[],  # Removed authors
                        journal=publication_info.get("summary", "Unknown Journal"),
                        abstract=result.get("snippet", "No abstract available."),
                        publication_date=publication_date,
                        keywords=[],
                        url=result.get("link", "No URL available"),
                        discipline=query,
                        citation_count=citations,
                    ))
                except Exception as e:
                    print(f"Error parsing article: {e}")

            return articles

        except Exception as e:
            print(f"Error fetching articles: {e}")
            return []

    @staticmethod
    def parse_publication_date(summary: str) -> Optional[datetime]:
        """
        Extract and parse the publication year from a summary string.
        """
        try:
            year = [int(s) for s in summary.split() if s.isdigit() and len(s) == 4][0]
            return datetime(year, 1, 1)
        except (IndexError, ValueError):
            return None

    @staticmethod
    def process_with_gpt(articles: List[Article], query: str) -> List[Article]:
        """
        Use GPT to refine and rank articles based on relevance and citation numbers.
        """
        openai.api_key = "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" # Replace with your OpenAI API key

        # Prepare prompt
        articles_text = "\n".join([
            f"Title: {article.title}\nJournal: {article.journal}\nAbstract: {article.abstract}\nYear: {article.publication_date.year if article.publication_date else 'Unknown'}\nCitations: {article.citation_count}\nLink: {article.url}\n"
            for article in articles
        ])
        prompt = f"""
        The following is a list of research articles related to "{query}":
        {articles_text}
        
        Please rank these articles based on relevance and citation counts and provide a cleaned list with the top 50 articles.
        Format the response as follows:
        Title: <title>
        Journal: <journal>
        Year: <year>
        Citations: <citations>
        Link: <link>
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert assistant for academic research."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=2000
            )

            formatted_text = response["choices"][0]["message"]["content"]
            return ResearchTools.parse_gpt_response(formatted_text, query)

        except Exception as e:
            print(f"Error enhancing articles with GPT: {e}")
            return []

    @staticmethod
    def parse_gpt_response(response_text: str, query: str) -> List[Article]:
        """
        Parse GPT's response into Article objects.
        """
        articles = []
        entries = response_text.split("\n\n")  # Assume articles are separated by double newlines

        for entry in entries:
            try:
                # Split entry into lines
                lines = entry.split("\n")
                if len(lines) < 5:
                    print(f"Skipping entry due to missing fields: {entry}")
                    continue

                # Extract fields
                title = lines[0].replace("Title:", "").strip()
                journal = lines[1].replace("Journal:", "").strip()
                year_str = lines[2].replace("Year:", "").strip()
                citations_str = lines[3].replace("Citations:", "").strip()
                url = lines[4].replace("Link:", "").strip()

                # Validate year
                year = int(year_str) if year_str.isdigit() else None
                citations = int(citations_str) if citations_str.isdigit() else 0

                # Construct Article object
                articles.append(Article(
                    title=title,
                    authors=[],  # Removed authors
                    journal=journal,
                    abstract="",  # Abstract not needed in the final table
                    publication_date=datetime(year, 1, 1) if year else None,
                    keywords=[],
                    url=url,
                    discipline=query,
                    citation_count=citations,
                ))

            except Exception as e:
                print(f"Error parsing GPT response: {entry}, Error: {e}")

        return articles
