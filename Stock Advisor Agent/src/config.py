STRATEGY_WEIGHTS = {
    "Balanced": {
        "value": 0.20, "quality": 0.20, "growth": 0.20,
        "momentum": 0.20, "risk": 0.20, "sentiment": 0.00
    },
    "Growth": {
        "value": 0.10, "quality": 0.20, "growth": 0.40,
        "momentum": 0.20, "risk": 0.10, "sentiment": 0.00
    },
    "Value": {
        "value": 0.40, "quality": 0.25, "growth": 0.10,
        "momentum": 0.10, "risk": 0.15, "sentiment": 0.00
    },
}

RATING_THRESHOLDS = {"Buy": 80, "Hold": 60, "Watch": 40}

TOP_N_PER_SECTOR = 5