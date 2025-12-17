from src.collectors.arxiv import fetch_arxiv
from src.collectors.europe_pmc import fetch_europe_pmc
from src.ingest.index import ingest

# Target corpus size (stop early once we reach this many valid docs)
TARGET_VALID_DOCS = 80

ARXIV_MAX_RESULTS = 80
EPMC_PAGE_SIZE = 80

# Fallback queries: broad -> more specific
QUERY_CANDIDATES = [
    "retrieval augmented generation",
    "RAG evaluation",
    "retrieval augmented generation evaluation",
    "RAG benchmarks",
    "LLM retrieval evaluation",
    "hallucination mitigation RAG",
    # keep your original intent last (most restrictive)
    "retrieval augmented generation evaluation benchmark metrics",
]

def collect_once(query: str):
    arxiv_docs = fetch_arxiv(query, max_results=ARXIV_MAX_RESULTS)
    epmc_docs = fetch_europe_pmc(query, page_size=EPMC_PAGE_SIZE)
    return arxiv_docs, epmc_docs

if __name__ == "__main__":
    all_docs = []
    used_query = None

    for q in QUERY_CANDIDATES:
        arxiv_docs, epmc_docs = collect_once(q)

        print(f"\n--- Trying query: {q!r} ---")
        print(f"arXiv raw docs: {len(arxiv_docs)}")
        print(f"EuropePMC raw docs: {len(epmc_docs)}")

        docs = []
        docs.extend(arxiv_docs)
        docs.extend(epmc_docs)

        valid = [d for d in docs if (d.get("text") or "").strip()]
        print(f"Valid docs (non-empty text): {len(valid)}")

        if len(valid) > 0:
            all_docs.extend(valid)
            used_query = q

        # Stop if we’ve reached our target corpus size
        if len(all_docs) >= TARGET_VALID_DOCS:
            break

    # De-dupe by URL (helps when overlap occurs)
    dedup = {}
    for d in all_docs:
        url = (d.get("metadata", {}) or {}).get("url") or ""
        key = url.strip() or (d.get("metadata", {}) or {}).get("title", "").strip()
        if key:
            dedup[key] = d

    final_docs = list(dedup.values())

    print("\n==============================")
    print("FINAL COLLECTION SUMMARY")
    print("==============================")
    print("Used query (first that returned docs):", used_query)
    print("Total valid docs collected:", len(all_docs))
    print("After de-dup:", len(final_docs))

    n = ingest(final_docs)
    print(f"✅ Ingested {n} documents into Chroma.")
