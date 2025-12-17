# 🧠 Research Assistant Agent  
### CrewAI · GPT-5.2 · Streamlit

A production-ready **multi-agent research assistant** built with **CrewAI**, **GPT-5.2**, and a **Streamlit UI**.

This system uses a *team of AI agents* to read real source documents, extract evidence, and generate a structured, executive-ready research brief — even in **restricted enterprise environments** where web search APIs are blocked.

![Application Interface](https://github.com/soudey123/AIAgentLab/blob/main/Research%20Assistant%20Agent/app_screenshot.png)

---

## 🔍 What This Project Does

- Accepts a **topic + list of URLs**
- Runs a **2-agent CrewAI workflow**
  - **Researcher Agent** → evidence extraction
  - **Summarizer Agent** → structured synthesis
- Outputs a **Markdown research report**
- Supports both:
  - **CLI execution**
  - **Interactive Streamlit UI**

---

## 🏗️ High-Level Architecture

![Research Agent Workflow](https://github.com/soudey123/AIAgentLab/blob/main/Research%20Assistant%20Agent/Research%20Agent%20Workflow.png))

---

## 📁 Project Structure

```
research-assistant-agent/
├── app.py                # Streamlit UI
├── requirements.txt
├── .env                  # API keys (not committed)
├── output/
│   └── report.md         # Generated research brief
└── src/
    ├── main.py           # CLI entry point
    ├── crew.py           # Agent + task definitions
    ├── tools.py          # Custom tools (URL fetch, URL mode)
    └── prompts.py        # Agent instructions
```

---

## ⚙️ Setup Instructions

### 1️⃣ Python Environment

Requires **Python 3.10+** (recommended: **Python 3.12**)

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```txt
crewai
streamlit
python-dotenv
requests
beautifulsoup4
```

---

### 3️⃣ Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ Never commit `.env` to source control.

---

## 🧠 Agent Design

### 🔍 Researcher Agent
- Reads user-provided URLs
- Fetches and cleans webpage content
- Extracts evidence and key findings
- Produces **research notes with sources**

### 📝 Summarizer Agent
- Consumes research notes only
- Creates a structured brief including:
  - Executive summary
  - Key insights
  - Risks / unknowns
  - Recommendations
  - Sources

### Why Two Agents?
Separating **research** from **summarization**:
- reduces hallucinations
- improves traceability
- mirrors real analyst workflows

---

## 🚀 Running the Agent

### Option 1: Command Line (Headless)

```bash
python -m src.main
```

Or pass a custom topic + URLs:

```bash
python -m src.main "AI Research Paper List" \
  https://arxiv.org/abs/1706.03762 \
  https://arxiv.org/abs/2303.08774
```

Output will be written to:

```
output/report.md
```

---

### Option 2: Streamlit UI (Recommended)

```bash
streamlit run app.py
```

**UI Features**
- Topic input
- URL input (one per line)
- Run button
- Live output preview
- Downloadable Markdown report
- Custom colorful styling

---

## 🌐 Why URL-Only Mode?

Many enterprise networks block:
- Google / Serper
- DuckDuckGo
- Wikipedia APIs

This project intentionally supports **URL-only mode**, making it:

- deterministic
- reliable
- production-friendly
- resistant to hallucinations

You control the sources → the agent cannot invent facts.

---

## 🧩 Extending the System

Easy upgrades:
- Add a **fact-checker agent**
- Add **citation validation**
- Add **comparison tables**
- Integrate **RAG / vector databases**
- Schedule runs (cron / Airflow)
- Deploy on Streamlit Cloud or internal infra

---

## 📌 Use Cases

- Competitive analysis
- Literature reviews
- Market research
- Technical deep dives
- Internal knowledge synthesis
- AI / ML paper summaries

---

## 📄 License

MIT (or your preferred license)

---

## ⭐ Acknowledgements

Built with:
- **CrewAI**
- **OpenAI GPT-5.2**
- **Streamlit**

---

If this project helped you, ⭐ the repo and share feedback!
