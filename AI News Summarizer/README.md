# AI News Summarizer 🤖 📰

An automated tool that fetches, summarizes, and emails the latest AI news using OpenAI's GPT and NewsAPI.

## Features ✨

- Fetches latest AI-related news articles from multiple sources
- Generates concise summaries using OpenAI's GPT
- Delivers summaries directly to your email
- Supports automated scheduling
- Cross-platform compatibility (Windows, macOS, Linux)

## Prerequisites 📋

- Python 3.7 or higher
- OpenAI API key
- News API key
- Gmail account with App Password enabled

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-news-summarizer.git
cd ai-news-summarizer
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

4. Update the `.env` file with your credentials:
```
OPENAI_API_KEY=your-openai-api-key
NEWS_API_KEY=your-news-api-key
EMAIL_USER=your-gmail-address
EMAIL_PASS=your-gmail-app-password
RECIPIENT_EMAIL=recipient-email
```

## Usage 💡

### Manual Execution

Run the script directly:
```bash
python src/news_summarizer.py
```

### Automated Scheduling

#### Windows (Task Scheduler)
1. Open Task Scheduler
2. Create a new Basic Task
3. Set trigger to Weekly
4. Action: Start a program
   - Program/script: `python`
   - Arguments: `path/to/src/scheduler.py`

#### macOS/Linux (Cron)
Add to crontab (runs every Monday at 9 AM):
```bash
0 9 * * 1 /usr/bin/python3 /path/to/src/scheduler.py
```

## Configuration ⚙️

### News Search Parameters
Modify in `src/config.py`:
```python
NEWS_PARAMS = {
    "q": "artificial intelligence OR AI",
    "pageSize": 5,
    "language": "en"
}
```

### Summary Style
Adjust the prompt template in `src/config.py`:
```python
SUMMARY_PROMPT = """
Your custom summarization instructions here...
"""
```

## File Structure 📁

- `src/news_summarizer.py`: Main script for fetching and summarizing news
- `src/scheduler.py`: Scheduling script for automated execution
- `src/config.py`: Configuration settings
- `tests/`: Unit tests
- `.env.example`: Example environment variables file
- `requirements.txt`: Required Python packages

## Running Tests 🧪

```bash
python -m pytest tests/
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- OpenAI for GPT API
- NewsAPI for news data
- All contributors to this project

## Contact 📧

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)
Project Link: [https://github.com/yourusername/ai-news-summarizer](https://github.com/yourusername/ai-news-summarizer)
