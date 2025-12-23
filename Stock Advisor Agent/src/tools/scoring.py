from typing import Dict, Any


def normalize(value: float, low: float, high: float) -> float:
    """
    Linearly normalize to 0–100 with clipping.
    """
    try:
        v = float(value)
    except (TypeError, ValueError):
        return 0.0

    if high == low:
        return 50.0

    if v <= low:
        return 0.0
    if v >= high:
        return 100.0

    return (v - low) / (high - low) * 100.0


def score_factors(metrics: Dict[str, Any]) -> Dict[str, float]:
    """
    Compute deterministic factor scores (0–100) from metrics.

    Expected keys in metrics:
      - pe_ratio (float)
      - roe (float, %)
      - revenue_growth (float, %)
      - momentum (float, %)
    """

    pe_ratio = float(metrics.get("pe_ratio") or 0.0)
    roe = float(metrics.get("roe") or 0.0)
    revenue_growth = float(metrics.get("revenue_growth") or 0.0)
    momentum = float(metrics.get("momentum") or 0.0)

    # Value: lower P/E is better; we convert to inverse-like score safely.
    # Clamp P/E to avoid division explosion.
    # If pe_ratio is 0 (unknown), treat as neutral-ish.
    if pe_ratio > 0:
        inv_pe = 1.0 / min(pe_ratio, 200.0)  # cap P/E at 200 for stability
        value_score = normalize(inv_pe, 0.0, 0.1)  # 0.1 ~ P/E=10
    else:
        value_score = 50.0

    # Quality: ROE typical range 0–30% for scoring
    quality_score = normalize(roe, 0.0, 30.0)

    # Growth: revenue growth 0–25% range for scoring (clip outside)
    growth_score = normalize(revenue_growth, 0.0, 25.0)

    # Momentum: map -20% to +40% into 0–100
    momentum_score = normalize(momentum, -20.0, 40.0)

    return {
        "value": round(value_score, 2),
        "quality": round(quality_score, 2),
        "growth": round(growth_score, 2),
        "momentum": round(momentum_score, 2),
    }


# Backwards-compatible aliases (if earlier code used different names)
score_factor_metrics = score_factors
compute_factor_scores = score_factors