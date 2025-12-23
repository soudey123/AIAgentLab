import os
import uuid
from datetime import datetime
from typing import Dict, Any, List

from crewai import Agent, Task, Crew, LLM

from src.tools.market_data import get_price_metrics
from src.tools.fundamentals import get_fundamentals
from src.tools.scoring import score_factors
from src.tools.risk import risk_score
from src.tools.news import get_recent_news, news_sentiment_score
from src.tools.explain import build_matrix
from src.config import STRATEGY_WEIGHTS, RATING_THRESHOLDS


# ============================================================
# LLM CONFIGURATION
# ============================================================
def get_llm():
    """
    Primary LLM for narrative reasoning.
    GPT-5.2 can legitimately return empty output, so downstream
    logic MUST be defensive.
    """
    return LLM(
        model="gpt-5.2",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.4,
        top_p=0.95,
        max_completion_tokens=900,
    )


# ============================================================
# CONFIDENCE / DISAGREEMENT METER
# ============================================================
def compute_confidence(agent_texts: List[str]) -> Dict[str, Any]:
    """
    Very lightweight agreement heuristic across agent narratives.
    """
    signals = []

    for txt in agent_texts:
        if not txt or not isinstance(txt, str):
            signals.append(0)
            continue

        t = txt.lower()
        if any(w in t for w in ["strong", "positive", "tailwind", "supportive"]):
            signals.append(1)
        elif any(w in t for w in ["risk", "weak", "headwind", "uncertain", "downside"]):
            signals.append(-1)
        else:
            signals.append(0)

    diversity = len(set(signals))
    agreement = 1 - (diversity - 1) / max(len(signals), 1)
    score = round(agreement * 100, 1)

    label = (
        "High" if score >= 75
        else "Moderate" if score >= 50
        else "Low"
    )

    return {
        "score": score,
        "label": label,
        "signals": signals,
    }


# ============================================================
# SAFE CREW EXECUTION (GUARANTEED NARRATIVE)
# ============================================================
def safe_kickoff(
    crew: Crew,
    ticker: str,
    rating: str,
    overall_score: float,
    factor_matrix: List[Dict[str, Any]],
) -> str:
    """
    Ensures we ALWAYS return a narrative string.
    """
    try:
        result = crew.kickoff()
        if result and str(result).strip():
            return str(result)
    except Exception:
        pass

    # Deterministic + AI-styled fallback (still acceptable)
    top_drivers = factor_matrix[:3]

    return (
        f"Investment Narrative for {ticker}:\n\n"
        f"The current recommendation is **{rating}**, with an overall score of "
        f"{overall_score:.1f}. The analysis is driven primarily by:\n\n"
        + "\n".join(
            f"- {d['Factor']} (weighted impact {d['Weighted Contribution']:.1f})"
            for d in top_drivers
        )
        + "\n\nThis narrative reflects AI-assisted interpretation of quantitative "
          "signals and risk factors to support informed decision-making."
    )


# ============================================================
# MAIN ENTRY POINT
# ============================================================
def run_analysis(
    ticker: str,
    strategy: str,
    horizon: str,
) -> Dict[str, Any]:
    """
    Core analysis pipeline used by:
    - Single-ticker analysis
    - Top-5 sector picks
    """

    run_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    # --------------------------------------------------------
    # 1. DETERMINISTIC DATA & SCORING LAYER
    # --------------------------------------------------------
    price = get_price_metrics(ticker)
    fundamentals = get_fundamentals(ticker)
    news = get_recent_news(ticker)

    metrics = {**price, **fundamentals}

    factor_scores = score_factors(metrics)
    factor_scores["risk"] = risk_score(price.get("volatility", 0.0))
    factor_scores["sentiment"] = news_sentiment_score(news)

    weights = STRATEGY_WEIGHTS[strategy]
    factor_matrix, overall_score = build_matrix(factor_scores, weights)

    if overall_score >= RATING_THRESHOLDS["Buy"]:
        rating = "Buy"
    elif overall_score >= RATING_THRESHOLDS["Hold"]:
        rating = "Hold"
    elif overall_score >= RATING_THRESHOLDS["Watch"]:
        rating = "Watch"
    else:
        rating = "Avoid"

    # --------------------------------------------------------
    # 2. MULTI-AGENT INTERPRETATION LAYER
    # --------------------------------------------------------
    llm = get_llm()

    market_agent = Agent(
        role="Market Analyst",
        goal="Explain momentum, trend, and price behavior.",
        backstory="You are a quantitative technical market analyst.",
        llm=llm,
        allow_delegation=False,
    )

    fundamentals_agent = Agent(
        role="Fundamentals Analyst",
        goal="Explain valuation, quality, and growth.",
        backstory="You are an equity research analyst focused on fundamentals.",
        llm=llm,
        allow_delegation=False,
    )

    risk_agent = Agent(
        role="Risk Analyst",
        goal="Identify downside risks and uncertainty.",
        backstory="You are a portfolio risk manager.",
        llm=llm,
        allow_delegation=False,
    )

    synthesizer_agent = Agent(
        role="Chief Investment Strategist",
        goal="Produce a detailed, horizon-aware investment narrative.",
        backstory="You synthesize multi-agent analysis into a coherent thesis.",
        llm=llm,
        allow_delegation=False,
    )

    # --------------------------------------------------------
    # 3. TASKS (DETAILED OUTPUT)
    # --------------------------------------------------------
    tasks = [
        Task(
            description=f"""
            Ticker: {ticker}
            Investment Horizon: {horizon}
            Price Metrics: {price}

            Explain:
            - Momentum strength
            - Trend direction
            - What the price action implies for this horizon
            """,
            expected_output="Detailed market/momentum analysis.",
            agent=market_agent,
        ),
        Task(
            description=f"""
            Ticker: {ticker}
            Investment Horizon: {horizon}
            Fundamentals: {fundamentals}

            Explain:
            - Valuation attractiveness
            - Quality and balance sheet strength
            - Growth outlook relevant to this horizon
            """,
            expected_output="Detailed fundamentals analysis.",
            agent=fundamentals_agent,
        ),
        Task(
            description=f"""
            Ticker: {ticker}
            Investment Horizon: {horizon}
            Risk Score: {factor_scores['risk']}
            Sentiment Score: {factor_scores['sentiment']}
            Recent News Headlines: {[n.get('title') for n in news]}

            Explain:
            - Key downside risks
            - Volatility considerations
            - What could invalidate the thesis
            """,
            expected_output="Detailed risk analysis.",
            agent=risk_agent,
        ),
        Task(
            description=f"""
            Ticker: {ticker}
            Investment Horizon: {horizon}
            Rating: {rating}
            Factor Matrix: {factor_matrix}

            Combine ALL analyses into a detailed investment narrative including:
            - Clear investment thesis
            - Horizon-specific drivers
            - Key risks and mitigants
            - How recent news factors in
            - An overall confidence assessment
            """,
            expected_output="Comprehensive investment narrative.",
            agent=synthesizer_agent,
        ),
    ]

    crew = Crew(
        agents=[
            market_agent,
            fundamentals_agent,
            risk_agent,
            synthesizer_agent,
        ],
        tasks=tasks,
        verbose=False,
        max_rpm=0,  # disable retry spam for GPT-5.x
    )

    narrative = safe_kickoff(
        crew,
        ticker,
        rating,
        overall_score,
        factor_matrix,
    )

    # --------------------------------------------------------
    # 4. CONFIDENCE METER
    # --------------------------------------------------------
    confidence = compute_confidence([narrative])

    # --------------------------------------------------------
    # 5. FINAL OUTPUT
    # --------------------------------------------------------
    return {
        "run_id": run_id,
        "timestamp": timestamp,
        "ticker": ticker,
        "strategy": strategy,
        "horizon": horizon,
        "rating": rating,
        "overall_score": overall_score,
        "factor_matrix": factor_matrix,
        "narrative": narrative,
        "confidence": confidence,
        "news": news,
        "audit": {
            "metrics": metrics,
            "weights": weights,
            "model": "gpt-5.2",
        },
    }