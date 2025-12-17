from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from src.common import CHROMA_DIR, CHROMA_COLLECTION


def retrieve(query: str, k: int = 5):
    db = Chroma(
        persist_directory=CHROMA_DIR,
        collection_name=CHROMA_COLLECTION,
        embedding_function=OpenAIEmbeddings()
    )
    return db.similarity_search(query, k=k)