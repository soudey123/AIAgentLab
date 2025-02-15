from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Email Configuration
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# News API Configuration
NEWS_PARAMS = {
    "q": os.getenv("NEWS_SEARCH_QUERY", "artificial intelligence OR AI"),
    "language": os.getenv("NEWS_LANGUAGE", "en"),
    "pageSize": int(os.getenv("NEWS_ARTICLE_COUNT", "5")),
    "sortBy": "relevancy"
}

# OpenAI Configuration
OPENAI_MODEL = "gpt-4"
OPENAI_TEMPERATURE = 0.7
OPENAI_MAX_TOKENS = 800

# Email Template
EMAIL_SUBJECT_TEMPLATE = "Weekly AI News Summary ({date})"
EMAIL_BODY_TEMPLATE = """
Hello,

Here is your AI news summary for the last week:

{summary}

Best regards,
Your AI Agent
"""

# Summary Prompt Template
SUMMARY_PROMPT = """
You are a helpful assistant specialized in summarizing news.
Below are several recent articles about AI. For each article:
- Provide a concise bullet-point summary of the key points.
- Include the provided link at the end of each bullet point.

{content}
"""