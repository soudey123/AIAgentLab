from pydantic import BaseModel
from typing import List, Dict

class Signal(BaseModel):
    factor: str
    raw_value: float
    score: float
    weight: float
    contribution: float
    rationale: str

class AgentResult(BaseModel):
    agent: str
    signals: List[Signal]
    score: float

class Recommendation(BaseModel):
    ticker: str
    strategy: str
    horizon: str
    overall_score: float
    rating: str
    agent_results: List[AgentResult]
    audit: Dict
