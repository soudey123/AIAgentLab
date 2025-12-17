# 🛡️ AegisRAG Intelligence Agent
**Evidence‑First RAG with LangGraph + LangChain**

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-enabled-green)
![LangGraph](https://img.shields.io/badge/LangGraph-orchestration-purple)
![VectorDB](https://img.shields.io/badge/VectorDB-Chroma-orange)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

AegisRAG is a **guarded, evidence‑first Retrieval‑Augmented Generation (RAG) system** built using **LangGraph** and **LangChain**.  
It is designed for **research and enterprise workflows** where **grounding, citations, and refusal on weak evidence** matter.

> 🚫 This project does **NOT** use CrewAI.  
> ✅ Orchestration is done via **LangGraph**.

---

## ✨ Key Features

- 🔎 **Public data ingestion** from **arXiv + Europe PMC (PubMed)**
- 🧠 **Vector search** using **Chroma**
- 🧩 **LangGraph workflow**: Retrieve → Synthesize
- 🛡️ **Guardrails**: context‑only answers, mandatory citations
- ❌ Explicit **“Insufficient evidence”** responses
- 🖥️ **CLI + Streamlit UI**
- 📄 **Markdown reports** with sources

---

## 🧠 System Architecture



---

## 📁 Project Structure

```
AegisRAG/
├── app.py                   # Streamlit UI
├── requirements.txt
├── .env                     # secrets (DO NOT COMMIT)
├── chroma_db/               # persisted vector store
└── src/
    ├── main_ingest.py       # data ingestion
    ├── main_query.py        # CLI query runner
    ├── collectors/          # arXiv + Europe PMC
    ├── ingest/              # embedding + indexing
    ├── rag/                 # retriever
    └── graph/               # LangGraph workflow
```

---

## ⚙️ Setup

### 1️⃣ Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install -U langchain-chroma
```

---

## 🔐 Configuration

Create `.env` in project root:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
CHROMA_DIR=./chroma_db
CHROMA_COLLECTION=research_corpus
```

---

## 📥 Ingest Data

```bash
python -m src.main_ingest
```

Clean rebuild:

```bash
rm -rf chroma_db
python -m src.main_ingest
```

---

## 🔎 Query (CLI)

```bash
python -m src.main_query
```

Example:
```
What evaluation methods are commonly used for retrieval‑augmented generation systems?
```

---

## 🖥️ Streamlit UI

```bash
streamlit run app.py
```

---

## 🛡️ Guardrails Philosophy

AegisRAG enforces:

- Context‑only answers
- Mandatory citations
- Explicit refusal when evidence is weak
- Separation of retrieval vs synthesis

This makes it suitable for:
- Research assistants
- Compliance‑sensitive domains
- Enterprise knowledge systems

---

## 🚀 Roadmap

- Evidence strength grading (strong / medium / weak)
- Query rewriter agent
- Source filters
- Evaluation harness
- Scheduled ingestion
- PDF ingestion

---

## 📜 License

MIT License
