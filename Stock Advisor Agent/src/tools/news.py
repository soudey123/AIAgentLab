import yfinance as yf

POSITIVE_WORDS = ["beat", "growth", "strong", "up", "surge", "record"]
NEGATIVE_WORDS = ["miss", "weak", "down", "drop", "risk", "cut"]


def get_recent_news(ticker: str, max_items: int = 5):
    try:
        news = yf.Ticker(ticker).news or []
        cleaned = []

        for n in news[:max_items]:
            title = n.get("title")
            if not title or not isinstance(title, str):
                continue

            cleaned.append({
                "title": title,
                "publisher": n.get("publisher", "Unknown"),
                "link": n.get("link", ""),
            })

        return cleaned

    except Exception:
        return []


def news_sentiment_score(news_items):
    """
    Returns sentiment score on 0–100 scale.
    50 = neutral.
    """
    if not news_items:
        return 50.0

    pos, neg = 0, 0

    for n in news_items:
        title = n.get("title", "")
        if not isinstance(title, str):
            continue

        t = title.lower()

        if any(w in t for w in POSITIVE_WORDS):
            pos += 1
        if any(w in t for w in NEGATIVE_WORDS):
            neg += 1

    score = 50 + (pos - neg) * 10
    return max(0.0, min(100.0, float(score)))
