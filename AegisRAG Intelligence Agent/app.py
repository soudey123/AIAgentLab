import os
from datetime import datetime
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from src.graph.rag_graph import app as rag_app

# ----------------------------
# Load .env reliably (project root)
# ----------------------------
ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env", override=True)

# ----------------------------
# Optional Opik imports (graceful)
# ----------------------------
OPIK_AVAILABLE = True
try:
    from opik import Opik
    from opik.evaluation.metrics import (
        Hallucination,
        AnswerRelevance,
        ContextRecall,
        ContextPrecision,
        Moderation,
    )
except Exception:
    OPIK_AVAILABLE = False


def _get_context_from_result(result: dict):
    """Try multiple keys in case rag_graph returns different structures."""
    for key in ["contexts", "context", "retrieved_context", "retrieved_chunks", "docs_text", "docs"]:
        val = result.get(key)
        if not val:
            continue
        if isinstance(val, str):
            return [val]
        if isinstance(val, list):
            return [x if isinstance(x, str) else str(x) for x in val]
    return []


def _safe_metric_call(metric_obj, payload: dict):
    # common callable patterns across metric implementations
    try:
        if callable(metric_obj):
            return metric_obj(payload)
    except Exception:
        pass

    for fn_name in ["score", "compute", "evaluate"]:
        fn = getattr(metric_obj, fn_name, None)
        if fn is None:
            continue
        try:
            return fn(payload)
        except TypeError:
            try:
                return fn(**payload)
            except Exception:
                pass
        except Exception:
            pass

    raise RuntimeError(f"Could not call metric: {metric_obj.__class__.__name__}")


def run_opik_eval(question: str, answer: str, contexts: list[str]):
    if not OPIK_AVAILABLE:
        return {"error": "Opik is not installed. Install with: pip install opik"}

    api_key = os.getenv("OPIK_API_KEY")
    workspace = os.getenv("OPIK_WORKSPACE")
    if not api_key or not workspace:
        return {"error": "Missing OPIK_API_KEY or OPIK_WORKSPACE in .env"}

    _ = Opik()

    payload = {
        "input": question,
        "output": answer,
        "context": contexts or [],
        "reference": "",
    }

    metrics = [
        Hallucination(),
        AnswerRelevance(),
        ContextRecall(),
        ContextPrecision(),
        Moderation(),
    ]

    scores = {}
    for m in metrics:
        name = m.__class__.__name__
        try:
            scores[name] = _safe_metric_call(m, payload)
        except Exception as e:
            scores[name] = f"⚠️ {e}"

    return {"scores": scores}


# ----------------------------
# Streamlit page config
# ----------------------------
st.set_page_config(
    page_title="🛡️ AegisRAG Intelligence Agent",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------
# UI Styling (fix white bar + remove top chrome)
# ----------------------------
st.markdown(
    """
    <style>
      /* Hide Streamlit chrome completely (fixes white bar) */
      header[data-testid="stHeader"] { display: none !important; }
      div[data-testid="stToolbar"] { display: none !important; }
      div[data-testid="stDecoration"] { display: none !important; }
      #MainMenu { visibility: hidden; }
      footer { visibility: hidden; }

      /* Remove extra top padding that Streamlit keeps even when header hidden */
      .block-container { padding-top: 0.8rem !important; }

      /* App background */
      .stApp {
        background: radial-gradient(circle at 10% 10%, #0b3d91 0%, #06162e 45%, #030712 100%);
        color: #ffffff;
      }

      /* Sidebar (left pane) non-white */
      section[data-testid="stSidebar"] {
        background: radial-gradient(circle at 20% 10%, rgba(34,211,238,0.16) 0%, rgba(99,102,241,0.10) 25%, rgba(3,7,18,0.95) 70%);
        border-right: 1px solid rgba(255,255,255,0.10);
      }
      section[data-testid="stSidebar"] .stMarkdown,
      section[data-testid="stSidebar"] label,
      section[data-testid="stSidebar"] p,
      section[data-testid="stSidebar"] span,
      section[data-testid="stSidebar"] div {
        color: rgba(255,255,255,0.92) !important;
      }

      /* Cards */
      .aegis-card {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px;
        padding: 18px 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
      }

      /* Pills */
      .pill {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        background: rgba(59,130,246,0.22);
        border: 1px solid rgba(59,130,246,0.35);
        font-size: 12px;
        margin-right: 8px;
      }

      .small-muted { opacity: 0.82; font-size: 13px; }

      /* Inputs */
      .stTextArea textarea { border-radius: 12px; }

      /* Buttons (Quick Actions) */
      .stButton > button {
        width: 100%;
        border-radius: 12px !important;
        font-weight: 750 !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        background: linear-gradient(90deg, rgba(34,211,238,0.28), rgba(99,102,241,0.34), rgba(236,72,153,0.20)) !important;
        color: rgba(255,255,255,0.95) !important;
        box-shadow: 0 10px 24px rgba(0,0,0,0.25);
      }
      .stButton > button:hover {
        filter: brightness(1.08);
        transform: translateY(-1px);
      }

      /* Download button matches theme */
      div[data-testid="stDownloadButton"] > button {
        border-radius: 12px !important;
        font-weight: 750 !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        background: linear-gradient(90deg, rgba(34,211,238,0.24), rgba(59,130,246,0.28), rgba(99,102,241,0.26)) !important;
        color: rgba(255,255,255,0.95) !important;
      }

      /* Neon Title */
      .neon-title {
        margin: 0.2rem 0 0.6rem 0;
        font-size: 2.4rem;
        font-weight: 900;
        letter-spacing: 0.2px;
        color: #A5F3FC;
        text-shadow:
          0 0 10px rgba(34,211,238,0.30),
          0 0 22px rgba(99,102,241,0.20);
      }

      /* Opik score cards */
      .score-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 12px;
        padding: 10px 12px;
        margin-bottom: 8px;
      }
      .score-title { font-weight: 700; font-size: 13px; opacity: 0.95; }
      .score-val { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }

    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header ---
st.markdown(
    """
    <div class="aegis-card">
      <span class="pill">Evidence-first</span>
      <span class="pill">Citations</span>
      <span class="pill">Guardrails</span>
      <div class="neon-title">🛡️ AegisRAG Intelligence Agent</div>
      <div class="small-muted">
        Ask a question. AegisRAG retrieves from your local Chroma corpus (arXiv + PubMed/Europe PMC ingestion) and answers using only retrieved evidence.
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# --- Sidebar controls ---
st.sidebar.header("⚙️ Controls")
show_raw = st.sidebar.checkbox("Show raw output", value=False)
save_report = st.sidebar.checkbox("Save report to /output", value=True)

st.sidebar.markdown("---")
st.sidebar.caption("Tip: Re-run ingestion anytime you change collection queries.")

st.sidebar.markdown("---")
st.sidebar.subheader("🧪 Opik Evaluation")

enable_opik = st.sidebar.checkbox(
    "Run Opik eval after each run",
    value=False,
    help="Runs Opik metrics on the generated answer using retrieved context.",
)

if enable_opik:
    if not OPIK_AVAILABLE:
        st.sidebar.error("Opik not installed. Run: pip install opik")
    else:
        ok_key = bool(os.getenv("OPIK_API_KEY"))
        ok_ws = bool(os.getenv("OPIK_WORKSPACE"))
        st.sidebar.write(f"OPIK_API_KEY: {'✅' if ok_key else '❌'}")
        st.sidebar.write(f"OPIK_WORKSPACE: {'✅' if ok_ws else '❌'}")

# --- Input ---
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    question = st.text_area(
        "Enter your research question",
        placeholder="e.g., What evaluation methods are commonly used for retrieval-augmented generation systems?",
        height=120,
    )

with col2:
    # IMPORTANT: Do NOT add any extra widgets above this card.
    # The “mystery button” usually comes from a stray widget created here.
    st.markdown('<div class="aegis-card">', unsafe_allow_html=True)
    st.markdown("### Quick Actions")
    run_clicked = st.button("🚀 Run AegisRAG", use_container_width=True)
    clear_clicked = st.button("🧹 Clear", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if clear_clicked:
    st.session_state.pop("last_answer", None)
    st.session_state.pop("last_md", None)
    st.session_state.pop("last_opik", None)
    st.rerun()

# --- Run ---
if run_clicked:
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Running retrieval + synthesis..."):
            result = rag_app.invoke({"question": question.strip(), "run_opik": True})
            answer = result.get("answer", "").strip()

        st.session_state["last_answer"] = answer
        st.session_state["last_md"] = answer

        if save_report:
            os.makedirs("output", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            fname = f"output/report_{ts}.md"
            with open(fname, "w", encoding="utf-8") as f:
                f.write(st.session_state["last_md"])
            st.success(f"Saved report → {fname}")

        if enable_opik:
            contexts = _get_context_from_result(result)
            with st.spinner("Running Opik evaluation..."):
                st.session_state["last_opik"] = run_opik_eval(question.strip(), answer, contexts)

# --- Display result ---
if "last_answer" in st.session_state:
    st.markdown("")
    st.markdown('<div class="aegis-card">', unsafe_allow_html=True)
    st.markdown("## 📌 Result")
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    if show_raw:
        st.code(st.session_state["last_answer"])
    else:
        st.markdown(st.session_state["last_answer"])

    st.write("")

    if "last_opik" in st.session_state and st.session_state["last_opik"]:
        st.markdown('<div class="aegis-card">', unsafe_allow_html=True)
        st.markdown("## 🧪 Opik Evaluation (Hallucination & RAG Quality)")
        opik_res = st.session_state["last_opik"]

        if "error" in opik_res:
            st.error(opik_res["error"])
        else:
            for k, v in opik_res.get("scores", {}).items():
                st.markdown(
                    f"""
                    <div class="score-card">
                        <div class="score-title">{k}</div>
                        <div class="score-val">{v}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")

    st.download_button(
        label="⬇️ Download Markdown report",
        data=st.session_state["last_md"].encode("utf-8"),
        file_name="aegisrag_report.md",
        mime="text/markdown",
        use_container_width=True,
    )
