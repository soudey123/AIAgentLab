from typing import Dict, List, Tuple, Any


def build_matrix(scored_factors: Dict[str, float], weights: Dict[str, float]) -> Tuple[List[Dict[str, Any]], float]:
    """
    Build an explainable factor matrix and compute weighted overall score.

    Inputs:
      scored_factors: {factor_name: score_0_100}
      weights: {factor_name: weight_0_1}

    Returns:
      matrix_rows: list of dict rows for UI display
      overall_score: weighted sum (0–100-ish depending on weights)
    """
    rows: List[Dict[str, Any]] = []
    total = 0.0

    for factor, score in scored_factors.items():
        w = float(weights.get(factor, 0.0))
        s = float(score)
        contrib = s * w
        total += contrib

        rows.append({
            "Factor": factor,
            "Raw Score (0-100)": round(s, 2),
            "Weight": round(w, 4),
            "Weighted Contribution": round(contrib, 2),
        })

    # Sort by biggest contributors for readability
    rows.sort(key=lambda r: r["Weighted Contribution"], reverse=True)

    return rows, round(total, 2)


# Backwards-compatible alias
build_factor_matrix = build_matrix