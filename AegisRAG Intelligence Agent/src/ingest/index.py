from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from src.common import CHROMA_DIR, CHROMA_COLLECTION


def ingest(docs) -> int:
    """
    Ingests a list of dicts:
    {
      "text": str,
      "metadata": dict
    }
    into a persistent Chroma collection.
    """
    embeddings = OpenAIEmbeddings()

    documents = [
        Document(
            page_content=d["text"],
            metadata=d.get("metadata", {})
        )
        for d in docs
        if d.get("text")
    ]

    if not documents:
        print("⚠️ No valid documents to ingest.")
        return 0

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
        collection_name=CHROMA_COLLECTION,
    )
    return len(documents)

