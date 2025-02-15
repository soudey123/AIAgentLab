import datetime
import requests
import smtplib
import openai
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Dict, Optional
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import config from src
from src import config

class NewsAPIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"

    def fetch_articles(self, days: int = 7) -> List[Dict]:
        """Fetch AI-related articles from the past specified days."""
        today = datetime.date.today()
        from_date = today - datetime.timedelta(days=days)

        params = config.NEWS_PARAMS.copy()
        params.update({
            "from": from_date.isoformat(),
            "to": today.isoformat(),
            "apiKey": self.api_key
        })

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json().get("articles", [])
        except requests.RequestException as e:
            print(f"Error fetching news: {e}")
            return []


class OpenAISummarizer:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    def _format_articles(self, articles: List[Dict]) -> str:
        """Format articles for the summary prompt."""
        content_list = []
        for idx, article in enumerate(articles, start=1):
            content_list.append(
                f"Article {idx}:\n"
                f"Title: {article.get('title', 'No Title')}\n"
                f"Description: {article.get('description', 'No Description')}\n"
                f"URL: {article.get('url', 'No URL')}\n"
            )
        return "\n".join(content_list)

    def summarize(self, articles: List[Dict]) -> Optional[str]:
        """Generate a summary of the provided articles using OpenAI."""
        if not articles:
            return None

        prompt = config.SUMMARY_PROMPT.format(
            content=self._format_articles(articles)
        )

        try:
            response = openai.ChatCompletion.create(
                model=config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant specialized in summarizing news."},
                    {"role": "user", "content": prompt}
                ],
                temperature=config.OPENAI_TEMPERATURE,
                max_tokens=config.OPENAI_MAX_TOKENS
            )
            return response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Error summarizing with OpenAI: {e}")
            return None


class EmailSender:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """Send an email with the provided subject and body."""
        msg = MIMEMultipart()
        msg["From"] = self.email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            print("Email sent successfully!")
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False


class NewsSummarizer:
    def __init__(self):
        self.news_client = NewsAPIClient(config.NEWS_API_KEY)
        self.summarizer = OpenAISummarizer(config.OPENAI_API_KEY)
        self.email_sender = EmailSender(config.EMAIL_USER, config.EMAIL_PASS)

    def run(self) -> bool:
        """Execute the complete news summarization process."""
        # Fetch articles
        articles = self.news_client.fetch_articles()
        if not articles:
            print("No articles found or error in fetching.")
            return False

        # Generate summary
        summary = self.summarizer.summarize(articles)
        if not summary:
            print("Error generating summary.")
            return False

        # Send email
        subject = config.EMAIL_SUBJECT_TEMPLATE.format(
            date=datetime.date.today()
        )
        body = config.EMAIL_BODY_TEMPLATE.format(summary=summary)

        return self.email_sender.send_email(
            config.RECIPIENT_EMAIL,
            subject,
            body
        )


def main():
    summarizer = NewsSummarizer()
    summarizer.run()


if __name__ == "__main__":
    main()