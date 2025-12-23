import os
from datetime import datetime
import streamlit as st

from src.graph.rag_graph import app as rag_app

st.set_page_config(
    page_title="🛡️ AegisRAG Intelligence Agent",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Simple colorful styling ---
st.markdown(
    """
    <style>
      .stApp {
        background: radial-gradient(circle at 10% 10%, #0b3d91 0%, #06162e 45%, #030712 100%);
        color: #ffffff;
      }
      .block-container { padding-top: 2rem; }
      .aegis-card {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px;
        padding: 18px 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
      }
      .pill {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        background: rgba(59,130,246,0.25);
        border: 1px solid rgba(59,130,246,0.35);
        font-size: 12px;
        margin-right: 8px;
      }
      .small-muted { opacity: 0.8; font-size: 13px; }
      .stTextArea textarea { border-radius: 12px; }
      .stButton button { border-radius: 12px; font-weight: 600; }
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
      <h1 style="margin: 0.2rem 0 0.6rem 0;">🛡️ AegisRAG Intelligence Agent</h1>
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

# --- Input ---
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    question = st.text_area(
        "Enter your research question",
        placeholder="e.g., What evaluation methods are commonly used for retrieval-augmented generation systems?",
        height=120,
    )

with col2:
    st.markdown('<div class="aegis-card">', unsafe_allow_html=True)
    st.markdown("### Quick Actions")
    run_clicked = st.button("🚀 Run AegisRAG", use_container_width=True)
    clear_clicked = st.button("🧹 Clear", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if clear_clicked:
    st.session_state.pop("last_answer", None)
    st.session_state.pop("last_md", None)
    st.rerun()

# --- Run ---
if run_clicked:
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Running retrieval + synthesis..."):
            result = rag_app.invoke({"question": question.strip()})
            answer = result.get("answer", "").strip()

        st.session_state["last_answer"] = answer
        st.session_state["last_md"] = answer  # already Markdown formatted by rag_graph.py

        # Save report
        if save_report:
            os.makedirs("output", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            fname = f"output/report_{ts}.md"
            with open(fname, "w", encoding="utf-8") as f:
                f.write(st.session_state["last_md"])
            st.success(f"Saved report → {fname}")

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

    # Download button
    st.download_button(
        label="⬇️ Download Markdown report",
        data=st.session_state["last_md"].encode("utf-8"),
        file_name="aegisrag_report.md",
        mime="text/markdown",
        use_container_width=True,
    )