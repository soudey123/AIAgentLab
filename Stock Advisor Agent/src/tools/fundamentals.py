import yfinance as yf


def get_fundamentals(ticker: str) -> dict:
    """
    Fetch basic fundamentals via yfinance and return a stable,
    transparent dict used by scoring.py.

    Keys returned (always present):
      - pe_ratio (float)
      - roe (float, %)
      - revenue_growth (float, %)
    """
    t = yf.Ticker(ticker)
    info = t.info or {}

    pe = info.get("trailingPE")
    roe = info.get("returnOnEquity")
    rev_g = info.get("revenueGrowth")

    # Normalize to safe numeric values
    pe_ratio = float(pe) if isinstance(pe, (int, float)) and pe > 0 else 0.0
    roe_pct = float(roe * 100) if isinstance(roe, (int, float)) else 0.0
    rev_growth_pct = float(rev_g * 100) if isinstance(rev_g, (int, float)) else 0.0

    return {
        "pe_ratio": round(pe_ratio, 4),
        "roe": round(roe_pct, 4),
        "revenue_growth": round(rev_growth_pct, 4),
    }


# Backwards-compatible aliases (in case earlier code used different names)
get_fundamental_metrics = get_fundamentals
get_fundamentals_features = get_fundamentals
