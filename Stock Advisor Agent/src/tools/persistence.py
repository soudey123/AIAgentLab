import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict

RUNS_DIR = Path("outputs/runs")
RUNS_DIR.mkdir(parents=True, exist_ok=True)


def save_run(ticker: str, payload: Dict[str, Any]) -> str:
    """
    Save a run payload to outputs/runs as JSON.
    Returns the saved file path as a string.
    """
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    safe_ticker = (ticker or "UNKNOWN").replace("/", "_").replace(" ", "_")
    path = RUNS_DIR / f"{safe_ticker}_{ts}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    return str(path)


# Backwards-compatible alias
persist_run = save_run
