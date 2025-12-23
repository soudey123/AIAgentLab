# src/evaluation/opik_eval.py

"""
Opik evaluation helpers for AegisRAG.

This module is OPTIONAL.
If OPIK_API_KEY / OPIK_WORKSPACE are not seçt, evaluation is skipped gracefully.
"""

import os
from typing import List, Dict, Optional


def opik_available() -> bool:
    return bool(
        os.getenv("OPIK_API_KEY")
        and os.getenv("OPIK_WORKSPACE")
    )


def evaluate_with_opik(
    question: str,
    answer: str,
    contexts: List[str],
    references: Optional[List[str]] = None,
) -> Dict:
    """
    Run hallucination / relevance evaluation using Opik.
    Returns a structured dict safe to surface in the UI.
    """

    if not opik_available():
        return {
            "status": "skipped",
            "reason": "Opik not configured"
        }

    from opik import Opik
    from opik.evaluation import evaluate
    from opik.evaluation.metrics import (
        Hallucination,
        AnswerRelevance,
        ContextRecall,
        ContextPrecision,
    )

    client = Opik()

    def evaluation_task(_):
        return {
            "input": question,
            "output": answer,
            "context": contexts,
            "reference": references or [],
        }

    metrics = [
        Hallucination(),
        AnswerRelevance(),
        ContextRecall(),
        ContextPrecision(),
    ]

    results = evaluate(
        experiment_name="aegisrag_live_eval",
        dataset=[{"id": "single"}],  # live, ad-hoc evaluation
        task=evaluation_task,
        scoring_metrics=metrics,
    )

    return {
        "status": "evaluated",
        "metrics": results
    }
