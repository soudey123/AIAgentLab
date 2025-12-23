import yfinance as yf
import numpy as np


def get_price_metrics(ticker: str, period: str = "1y") -> dict:
    """
    Download OHLCV data and compute transparent price-based metrics.

    Returns:
      - momentum_6m (%)
      - volatility_annualized (%)
      - last_close
    """
    df = yf.download(ticker, period=period, progress=False)

    if df is None or df.empty or "Close" not in df.columns:
        raise ValueError(f"No price data returned for {ticker}. Try another ticker or period.")

    close = df["Close"].dropna()
    if len(close) < 30:
        raise ValueError(f"Not enough price history for {ticker} (need >= 30 trading days).")

    returns = close.pct_change().dropna()

    # 6 months ~ 126 trading days; if shorter history, fall back to available window
    lookback = 126 if len(close) > 126 else max(5, len(close) - 1)
    momentum_6m = (close.iloc[-1] / close.iloc[-lookback] - 1) * 100

    volatility_annualized = returns.std() * np.sqrt(252) * 100

    return {
        "momentum": float(round(momentum_6m, 2)),
        "volatility": float(round(volatility_annualized, 2)),
        "last_close": float(round(close.iloc[-1], 2)),
    }


# Backwards-compatible alias (if any other modules referenced old names)
get_price_features = get_price_metrics