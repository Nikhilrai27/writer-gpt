from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings

from src.config import (
    HUGGINGFACEHUB_API_TOKEN,
    CHROMA_PERSIST_DIR,
    CHROMA_COLLECTION_NAME,
)


embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
)

vectorstore = Chroma(
    collection_name=CHROMA_COLLECTION_NAME,
    embedding_function=embeddings,
    persist_directory=CHROMA_PERSIST_DIR,
)


def retrieve_context(query: str, k: int = 3) -> str:
    results = vectorstore.similarity_search(query, k=k)
    return "\n\n".join(doc.page_content for doc in results)
