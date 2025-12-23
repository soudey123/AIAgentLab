import os
from typing import Dict, Any, List

from dotenv import load_dotenv
from opik import Opik
from opik.evaluation import evaluate
from opik.evaluation.metrics import (
    Hallucination,
    AnswerRelevance,
    ContextRecall,
    ContextPrecision,
)

from src.graph.rag_graph import app as rag_app

# Load .env from project root when running as module
load_dotenv(override=True)

DATASET_NAME = os.getenv("OPIK_DATASET_NAME", "aegisrag_eval_set")
EXPERIMENT_NAME = os.getenv("OPIK_EXPERIMENT_NAME", "aegisrag_v1")
TOP_K = int(os.getenv("RAG_TOP_K", "8"))

client = Opik()
dataset = client.get_dataset(name=DATASET_NAME)


def _docs_to_context(docs: List[Any], max_docs: int = 8, max_chars_each: int = 1200) -> List[str]:
    ctx = []
    for d in (docs or [])[:max_docs]:
        txt = (getattr(d, "page_content", "") or "").strip()
        if txt:
            ctx.append(txt[:max_chars_each])
    return ctx


def evaluation_task(dataset_item: Dict[str, Any]) -> Dict[str, Any]:
    """
    Opik dataset rows should contain:
      - input: str (question)
    Optional:
      - reference: str (expected answer)
    """
    question = dataset_item["input"]

    result = rag_app.invoke({"question": question, "k": TOP_K})
    answer = result.get("answer", "")
    docs = result.get("docs", [])

    context = _docs_to_context(docs)

    return {
        "input": question,
        "output": answer,
        "reference": dataset_item.get("reference", ""),
        "context": context,
    }


metrics = [
    Hallucination(),
    AnswerRelevance(),
    ContextRecall(),
    ContextPrecision(),
]


def main():
    print(f"Running Opik batch eval | dataset={DATASET_NAME} | experiment={EXPERIMENT_NAME} | top_k={TOP_K}")
    eval_results = evaluate(
        experiment_name=EXPERIMENT_NAME,
        dataset=dataset,
        task=evaluation_task,
        scoring_metrics=metrics,
    )
    print("✅ Evaluation complete.")
    print(eval_results)


if __name__ == "__main__":
    main()
