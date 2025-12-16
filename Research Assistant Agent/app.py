import time
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from src.crew import build_crew
from src.tools import write_file

# Load .env reliably from project root
ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

st.set_page_config(
    page_title="Research Assistant Agent (CrewAI)",
    page_icon="🧠",
    layout="wide",
)

# ---------- Colorful UI styling ----------
st.markdown(
    """
    <style>
      /* --- Remove Streamlit top chrome spacing --- */
      header[data-testid="stHeader"] { 
        height: 0rem; 
        background: transparent; 
      }
      div[data-testid="stToolbar"] { visibility: hidden; height: 0; }
      div[data-testid="stDecoration"] { visibility: hidden; height: 0; }
      #MainMenu { visibility: hidden; }
      footer { visibility: hidden; }

      /* --- Page background --- */
      .stApp {
        background: radial-gradient(circle at top left, #0b1220 0%, #050814 45%, #050512 100%);
        color: #ffffff;
      }

      /* Reduce top padding so badge/title aren't clipped */
      .block-container { padding-top: 0.75rem; padding-bottom: 2rem; }

      h1, h2, h3, h4 { color: #EAF2FF; }

      .subtitle {
        font-size: 1.05rem;
        color: #c7d2fe;
        margin-top: -0.25rem;
        margin-bottom: 0.5rem;
      }

      .badge {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 700;
        background: linear-gradient(90deg, #22c55e, #06b6d4, #6366f1);
        color: #061024;
        margin-bottom: 0.75rem;
      }

      .card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 18px;
        padding: 18px 18px 10px 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.35);
      }

      .hint { font-size: 0.95rem; color: #a5b4fc; }

      /* ✅ IMPORTANT: Scope input styling ONLY inside cards */
      .card .stTextInput > div > div,
      .card .stTextArea > div > div {
        background: rgba(255,255,255,0.06) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
      }

      .stButton > button {
        background: linear-gradient(90deg, #7c3aed, #2563eb, #06b6d4) !important;
        color: white !important;
        border: 0 !important;
        border-radius: 14px !important;
        padding: 0.65rem 1.1rem !important;
        font-weight: 800 !important;
      }
      .stButton > button:hover { filter: brightness(1.08); transform: translateY(-1px); }

      .danger {
        background: rgba(239,68,68,0.12);
        border: 1px solid rgba(239,68,68,0.30);
        padding: 10px 12px;
        border-radius: 14px;
        color: #fecaca;
      }
      .ok {
        background: rgba(34,197,94,0.12);
        border: 1px solid rgba(34,197,94,0.30);
        padding: 10px 12px;
        border-radius: 14px;
        color: #bbf7d0;
      }
      code, pre {
        background: rgba(255,255,255,0.06) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Header ----------
st.markdown("<span class='badge'>CrewAI • GPT-5.2 • Research + Summarize</span>", unsafe_allow_html=True)
st.title("🧠 Research Assistant Agent")
st.markdown(
    "<div class='subtitle'>Paste a topic + (recommended) a few URLs, then run a 2-agent crew: Researcher → Summarizer.</div>",
    unsafe_allow_html=True,
)

# ---------- Layout ----------
left, right = st.columns([1.05, 1.2], gap="large")

with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("1) Configure your run")

    topic = st.text_input(
        "Topic",
        value="Competitive analysis: AI agent platforms for research + summarization",
        help="Describe what you want the research assistant team to produce."
    )

    st.markdown("**Sources (URLs)**")
    st.markdown(
        "<div class='hint'>Your network blocks many search endpoints. URL mode is the most reliable. "
        "Paste 3–10 URLs (docs/product pages/pricing/security pages).</div>",
        unsafe_allow_html=True,
    )

    urls_text = st.text_area(
        "One URL per line",
        value="\n".join([
            "https://docs.crewai.com/",
            "https://python.langchain.com/docs/langgraph/",
            "https://docs.llamaindex.ai/",
        ]),
        height=140,
    )

    # Optional toggles
    try_search = st.toggle(
        "Try web_search if URL list is empty",
        value=False,
        help="If enabled, the agent may try the web_search tool when no URLs are provided. On restricted networks this may fail."
    )

    save_name = st.text_input("Output filename", value="report.md")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("2) Run")

    run_btn = st.button("🚀 Run Research Crew")

    st.markdown(
        "<div class='hint'>Tip: If you see 403/blocked errors, paste URLs directly (product docs pages are ideal).</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Output")
    output_placeholder = st.empty()
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Run logic ----------
def parse_urls(text: str):
    urls = []
    for line in (text or "").splitlines():
        line = line.strip()
        if not line:
            continue
        # basic cleanup
        if line.startswith("- "):
            line = line[2:].strip()
        urls.append(line)
    return urls

if run_btn:
    urls = parse_urls(urls_text)

    if not topic.strip():
        st.error("Please enter a topic.")
        st.stop()

    if not urls and not try_search:
        st.markdown(
            "<div class='danger'>No URLs provided and web_search is disabled. "
            "Paste a few URLs or enable web_search.</div>",
            unsafe_allow_html=True,
        )
        st.stop()

    with st.spinner("Running agents… (Researcher → Summarizer)"):
        try:
            # If you want the crew to attempt search when urls is empty, just pass None.
            # If you pass an empty list [], the crew will treat it as 'provided URLs = none' (depending on your build_crew logic).
            urls_arg = urls if urls else (None if try_search else [])

            crew = build_crew(topic, urls=urls_arg)
            result = crew.kickoff()
            result_text = str(result)

            out_path = f"output/{save_name}"
            write_file(out_path, result_text)

            st.markdown("<div class='ok'>✅ Done! Saved to <b>output/</b>.</div>", unsafe_allow_html=True)
            output_placeholder.markdown(result_text)

            # Download button
            st.download_button(
                label="⬇️ Download report",
                data=result_text.encode("utf-8"),
                file_name=save_name,
                mime="text/markdown",
            )

        except Exception as e:
            st.markdown(
                f"<div class='danger'><b>Run failed:</b><br>{e}</div>",
                unsafe_allow_html=True,
            )