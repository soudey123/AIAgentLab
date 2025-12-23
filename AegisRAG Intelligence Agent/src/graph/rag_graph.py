# src/graph/rag_graph.py

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional, TypedDict

from langgraph.graph import StateGraph, END

from src.rag.retriever import retrieve


# ---------------------------
# Optional Opik evaluation
# ---------------------------
def _safe_opik_eval(
    *,
    question: str,
    answer: str,
    contexts: List[str],
    sources: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Runs Opik evaluation if available + configured.
    Never raises; returns a small dict safe for UI display.
    """
    try:
        from src.evaluation.opik_eval import evaluate_with_opik, opik_available

        if not opik_available():
            return {
                "status": "skipped",
                "reason": "Opik not configured (missing OPIK_API_KEY / OPIK_WORKSPACE)",
            }

        # references can be URLs/titles, helps some metrics
        references = []
        for s in (sources or [])[:20]:
            references.append(s.get("url") or s.get("title") or "")

        return evaluate_with_opik(
            question=question,
            answer=answer,
            contexts=contexts,
            references=references,
        )
    except Exception as e:
        return {"status": "error", "reason": f"Opik eval failed: {e}"}


# ---------------------------
# State
# ---------------------------
class RAGState(TypedDict, total=False):
    question: str
    k: int
    docs: List[Any]                 # LangChain Document list
    contexts: List[str]             # extracted text chunks
    sources: List[Dict[str, Any]]   # normalized sources
    answer: str                     # markdown answer
    run_opik: bool
    opik: Dict[str, Any]


# ---------------------------
# Helpers
# ---------------------------
def _doc_text(doc: Any) -> str:
    """Extract text from a LangChain Document or unknown object safely."""
    if doc is None:
        return ""
    # LangChain Document
    if hasattr(doc, "page_content"):
        return doc.page_content or ""
    # fallback (in case your retriever returns dicts later)
    if isinstance(doc, dict):
        return doc.get("text") or doc.get("page_content") or ""
    return str(doc)


def _doc_meta(doc: Any) -> Dict[str, Any]:
    """Extract metadata from a LangChain Document safely."""
    if doc is None:
        return {}
    if hasattr(doc, "metadata") and isinstance(doc.metadata, dict):
        return doc.metadata
    if isinstance(doc, dict):
        m = doc.get("metadata")
        return m if isinstance(m, dict) else {}
    return {}


def _normalize_sources(docs: List[Any]) -> List[Dict[str, Any]]:
    sources: List[Dict[str, Any]] = []
    seen = set()

    for d in docs or []:
        meta = _doc_meta(d)

        title = meta.get("title") or meta.get("paper_title") or "Untitled"
        url = meta.get("url") or meta.get("source") or meta.get("link") or ""
        provider = meta.get("provider") or meta.get("collection") or meta.get("origin") or ""
        year = meta.get("year") or meta.get("published") or ""

        key = (title, url)
        if key in seen:
            continue
        seen.add(key)

        sources.append(
            {
                "title": title,
                "url": url,
                "provider": provider,
                "year": year,
            }
        )

    return sources


def _format_sources_md(sources: List[Dict[str, Any]]) -> str:
    if not sources:
        return "_None (no retrieved sources)_"

    lines = []
    for i, s in enumerate(sources, start=1):
        title = s.get("title") or "Untitled"
        url = s.get("url") or ""
        provider = s.get("provider") or ""
        year = s.get("year") or ""

        meta_bits = [b for b in [provider, str(year) if year else ""] if b]
        meta = " — ".join(meta_bits).strip(" — ")

        if url:
            lines.append(f"[{i}] {title} — {meta} — {url}".strip())
        else:
            lines.append(f"[{i}] {title} — {meta}".strip())

    return "\n".join(lines)


def _get_llm():
    """
    Uses LangChain OpenAI chat model.
    Set OPENAI_MODEL in .env if needed. Default: gpt-5.2
    """
    try:
        from langchain_openai import ChatOpenAI
    except Exception as e:
        raise ImportError(
            "Missing langchain_openai. Install with: pip install -U langchain-openai"
        ) from e

    model = os.getenv("OPENAI_MODEL", "gpt-5.2")
    return ChatOpenAI(model=model, temperature=0.2)


# ---------------------------
# Graph nodes
# ---------------------------
def node_retrieve(state: RAGState) -> RAGState:
    question = (state.get("question") or "").strip()
    k = int(state.get("k") or 5)

    # ✅ retrieve(query=..., k=...) returns List[Document]
    docs = retrieve(query=question, k=k)

    contexts: List[str] = []
    for d in docs or []:
        t = _doc_text(d)
        t = " ".join(t.split())
        if t:
            contexts.append(t)

    sources = _normalize_sources(docs or [])

    return {
        **state,
        "docs": docs or [],
        "contexts": contexts,
        "sources": sources,
    }


def node_synthesize(state: RAGState) -> RAGState:
    question = (state.get("question") or "").strip()
    contexts = state.get("contexts") or []
    sources = state.get("sources") or []

    if not contexts:
        md = (
            "### Answer\n"
            "Insufficient evidence.\n\n"
            "### Evidence\n"
            "- No retrievable evidence was found in the local Chroma corpus.\n\n"
            "### What’s missing / Unknowns\n"
            "- More relevant documents in Chroma (try re-running ingestion with a tighter query).\n\n"
            "---\n"
            "### Sources\n"
            f"{_format_sources_md(sources)}"
        )
        return {**state, "answer": md}

    llm = _get_llm()

    joined_context = "\n\n".join([f"[CTX {i+1}] {c}" for i, c in enumerate(contexts[:12])])

    system = (
        "You are AegisRAG, an evidence-first research assistant.\n"
        "Rules:\n"
        "- Use ONLY the provided context.\n"
        "- If the context does not support an answer, say 'Insufficient evidence.'\n"
        "- Provide citations using bracket numbers like [1][2] that refer to the Sources list.\n"
        "- Do NOT invent sources.\n"
        "- Output in markdown with sections:\n"
        "  ### Answer\n"
        "  ### Evidence\n"
        "  ### What’s missing / Unknowns\n"
        "  ---\n"
        "  ### Sources\n"
    )

    user = (
        f"Question:\n{question}\n\n"
        f"Context (retrieved):\n{joined_context}\n\n"
        "Now answer using ONLY the context. If you cite, use [n] where n is a source number.\n"
    )

    resp = llm.invoke(
        [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
    )
    draft = resp.content if hasattr(resp, "content") else str(resp)

    # Always attach sources block at end (keep report stable)
    sources_md = _format_sources_md(sources)
    if "### Sources" not in draft:
        draft = f"{draft}\n\n---\n### Sources\n{sources_md}"
    else:
        if sources_md and sources_md not in draft:
            draft = f"{draft}\n\n{sources_md}"

    return {**state, "answer": draft.strip()}


def node_opik_eval(state: RAGState) -> RAGState:
    question = (state.get("question") or "").strip()
    answer = (state.get("answer") or "").strip()
    contexts = state.get("contexts") or []
    sources = state.get("sources") or []

    opik_result = _safe_opik_eval(
        question=question,
        answer=answer,
        contexts=contexts[:12],
        sources=sources,
    )

    return {**state, "opik": opik_result}


def should_run_opik(state: RAGState) -> str:
    return "opik" if bool(state.get("run_opik")) else "skip"


# ---------------------------
# Build graph
# ---------------------------
graph = StateGraph(RAGState)

graph.add_node("retrieve", node_retrieve)
graph.add_node("synthesize", node_synthesize)
graph.add_node("opik", node_opik_eval)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "synthesize")

graph.add_conditional_edges(
    "synthesize",
    should_run_opik,
    {"opik": "opik", "skip": END},
)

graph.add_edge("opik", END)

app = graph.compile()
