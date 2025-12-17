import requests

BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

def fetch_europe_pmc(query: str, page_size: int = 20):
    params = {
        "query": f'TITLE:"{query}" OR ABSTRACT:"{query}"',
        "format": "json",
        "pageSize": page_size,
        "resultType": "core",
    }

    r = requests.get(BASE, params=params, timeout=30)
    r.raise_for_status()

    data = r.json().get("resultList", {}).get("result", [])
    docs = []

    for item in data:
        abstract = item.get("abstractText")
        title = item.get("title") or ""
        text = (abstract or title).strip()

        if not text:
            continue

        pmid = item.get("pmid")
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else ""

        docs.append({
            "text": text,
            "metadata": {
                "source": "europe_pmc",
                "title": title,
                "url": url,
                "published": item.get("pubYear") or ""
            }
        })

    return docs