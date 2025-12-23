from typing import TypedDict, List, Any, Dict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

from src.rag.retriever import retrieve

# ---- LLM ----
llm = ChatOpenAI(model="gpt-5.2")

# ---- Graph State ----
class State(TypedDict):
    question: str
    docs: List[Any]
    answer: str


def retrieve_node(state: State) -> Dict[str, Any]:
    """Retrieve top-k docs from Chroma."""
    question = state["question"].strip()
    docs = retrieve(question, k=10)  # bump k for better coverage
    return {"docs": docs}


def synthesize_node(state: State) -> Dict[str, Any]:
    """Synthesize an evidence-grounded answer WITH citations and a sources section."""
    docs = state.get("docs", [])

    # Build context + source list
    context_blocks = []
    sources_lines = []

    for i, d in enumerate(docs, start=1):
        text = (getattr(d, "page_content", "") or "").strip()
        md = getattr(d, "metadata", {}) or {}

        title = (md.get("title") or "Untitled").strip()
        url = (md.get("url") or "").strip()
        source = (md.get("source") or "").strip()
        published = (md.get("published") or "").strip()

        # Keep context compact but useful
        if text:
            context_blocks.append(f"[Doc {i}] {text}")

        # Always include sources even if text is empty (rare)
        meta_bits = " | ".join([b for b in [source, published] if b])
        if meta_bits:
            sources_lines.append(f"[{i}] {title} — {meta_bits} — {url}")
        else:
            sources_lines.append(f"[{i}] {title} — {url}")

    context = "\n\n".join(context_blocks).strip()
    sources_text = "\n".join(sources_lines).strip()

    # Guardrail: if retrieval came back empty, refuse cleanly
    if not context:
        answer = (
            "Insufficient evidence.\n\n"
            "I couldn't retrieve any usable context from the vector database for this question.\n"
            "Try re-ingesting with a broader query, increasing k, or asking a more specific question.\n\n"
            "---\n### Sources\n"
            + (sources_text or "(No sources retrieved.)")
        )
        return {"answer": answer}

    prompt = f"""
You are AegisRAG, a guarded research assistant.

Your job:
- Answer using ONLY the Context below.
- If the Context does not support a strong answer, say "Insufficient evidence."
- Do NOT guess or bring in outside knowledge.
- Every claim must have citations using bracket numbers like [1], [2] that refer to the Sources list.

Write the output in this structure:

### Answer
(Concise answer with citations)

### Evidence
- Bullet points quoting or paraphrasing supported facts (each bullet has citations)

### What’s missing / Unknowns
- Bullet points of what would be needed to fully answer (if applicable)

Question:
{state["question"]}

Context:
{context}

Sources:
{sources_text}
""".strip()

    response = llm.invoke(prompt)
    body = (response.content or "").strip()

    # Append sources section at end (always)
    final = body + "\n\n---\n### Sources\n" + sources_text
    return {"answer": final}


# ---- Build graph ----
graph = StateGraph(State)
graph.add_node("retrieve", retrieve_node)
graph.add_node("synthesize", synthesize_node)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "synthesize")
graph.add_edge("synthesize", END)

app = graph.compile()