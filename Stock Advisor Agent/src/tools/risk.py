def risk_score(volatility: float) -> float:
    """
    Deterministic risk scoring based on annualized volatility (%).
    Returns a 0–100 score where higher = lower risk.
    Transparent banding (easy to explain in UI).
    """
    try:
        vol = float(volatility)
    except (TypeError, ValueError):
        return 50.0  # neutral if unknown

    if vol < 15:
        return 90.0
    elif vol < 25:
        return 70.0
    elif vol < 40:
        return 50.0
    else:
        return 30.0


# Backwards-compatible alias (if older code used different names)
compute_risk_score = risk_score