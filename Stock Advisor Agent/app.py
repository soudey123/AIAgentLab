import streamlit as st
import pandas as pd

from src.crew import run_analysis
from src.tools.universe import SECTOR_UNIVERSE
from src.tools.persistence import save_run

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="AI Stock Advisor (Multi-Agent)",
    page_icon="📈",
    layout="wide",
)

# ------------------------------------------------
# 🔥 STREAMLIT-COMPATIBLE CSS (INLINE)
# ------------------------------------------------
st.markdown(
    """
    <style>
    /* =======================
       APP BACKGROUND
    ======================= */
    .stApp {
        background: linear-gradient(135deg, #0a1f44, #0b3c91);
        color: #f8fafc;
        font-family: Inter, system-ui;
    }

    /* =======================
       HEADERS
    ======================= */
    h1, h2, h3 {
        color: #e0f2fe;
        font-weight: 800;
    }

    /* =======================
       INPUTS
    ======================= */
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] {
        background-color: #0f2a5c !important;
        color: #e0f2fe !important;
        border-radius: 12px;
        border: 1px solid rgba(186,230,253,.4);
    }

    /* =======================
       BUTTONS
    ======================= */
    .stButton button {
        background: linear-gradient(90deg, #38bdf8, #2563eb);
        color: white;
        font-weight: 800;
        border-radius: 14px;
        border: none;
        padding: 0.6rem 1.4rem;
    }

    .stButton button:hover {
        background: linear-gradient(90deg, #0ea5e9, #1d4ed8);
        transform: scale(1.02);
    }

    /* =======================
       CARDS
    ======================= */
    .card {
        background: linear-gradient(145deg, #0f2a5c, #0b1f3a);
        border-radius: 18px;
        padding: 1.4rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 12px 30px rgba(0,0,0,.4);
        border: 1px solid rgba(186,230,253,.25);
    }

    /* =======================
       TABS
    ======================= */
    button[data-baseweb="tab"] {
        font-weight: 700;
        color: #bae6fd;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #38bdf8;
        border-bottom: 3px solid #38bdf8;
    }

    /* =======================
       DATAFRAME
    ======================= */
    thead tr th {
        background-color: #0b3c91 !important;
        color: #e0f2fe !important;
    }

    tbody tr td {
        background-color: #0a2558 !important;
        color: #f8fafc !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------
# HEADER
# ------------------------------------------------
st.title("📈 AI Stock Advisor — Multi-Agent Intelligence")

# ------------------------------------------------
# TABS
# ------------------------------------------------
tab1, tab2, tab3 = st.tabs(
    ["🔍 Analyze a Stock", "🏆 Top-5 Stocks by Sector", "📘 How to Use / Glossary"]
)

# =================================================
# TAB 1 — SINGLE STOCK
# =================================================
with tab1:
    st.subheader("Analyze a Single Stock")

    col1, col2, col3 = st.columns(3)

    with col1:
        ticker = st.text_input("Ticker", "AAPL").upper()

    with col2:
        strategy = st.selectbox("Strategy", ["Balanced", "Growth", "Value"])

    with col3:
        horizon = st.selectbox(
            "Investment Horizon",
            ["1 Month", "3 Months", "6 Months", "1 Year"],
            index=2,
        )

    if st.button("Run Analysis"):
        with st.spinner("Running multi-agent analysis…"):
            result = run_analysis(ticker, strategy, horizon)

        st.markdown(
            f"""
            <div class="card">
                <h2>{result['ticker']} — {result['rating']} ({result['overall_score']:.1f})</h2>
                <p><b>Strategy:</b> {strategy} | <b>Horizon:</b> {horizon}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 🧠 AI Narrative")
        st.write(result["narrative"])

        st.markdown("### 📊 Factor Matrix")
        st.dataframe(pd.DataFrame(result["factor_matrix"]))

        save_run(ticker, result)

# =================================================
# TAB 2 — TOP 5 (FAST)
# =================================================
with tab2:
    st.subheader("Top-5 Stocks by Sector")

    c1, c2, c3 = st.columns(3)

    with c1:
        sector = st.selectbox("Sector", list(SECTOR_UNIVERSE.keys()))

    with c2:
        strategy_2 = st.selectbox("Strategy", ["Balanced", "Growth", "Value"], key="s2")

    with c3:
        horizon_2 = st.selectbox(
            "Investment Horizon",
            ["1 Month", "3 Months", "6 Months", "1 Year"],
            key="h2",
        )

    if st.button("Generate Top-5 Picks"):
        st.success("Top-5 generation optimized for speed 🚀")

        for t in SECTOR_UNIVERSE[sector][:5]:
            res = run_analysis(t, strategy_2, horizon_2)
            st.markdown(
                f"""
                <div class="card">
                    <h3>{res['ticker']} — {res['rating']} ({res['overall_score']:.1f})</h3>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write(res["narrative"])

# =================================================
# TAB 3 — README
# =================================================
with tab3:
    st.subheader("📘 How to Use This App")

    st.markdown(
        """
        <div class="card">
        <b>This app combines:</b>
        <ul>
          <li>Quantitative finance signals</li>
          <li>Multi-agent AI reasoning</li>
          <li>Transparent factor scoring</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("📈 Ticker Symbols"):
        st.write("Short codes for stocks like AAPL (Apple), MSFT (Microsoft).")

    with st.expander("⚙️ Strategy"):
        st.write("Balanced = equal weights, Growth = momentum, Value = valuation.")

    with st.expander("🔎 Confidence Meter"):
        st.write("Measures agreement across AI agents.")

    st.info("Educational use only. Not financial advice.")
