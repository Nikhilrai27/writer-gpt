import os
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings

load_dotenv()

embeddings=HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=os.getenv
    ("HUGGINGFACEHUB_API_TOKEN")
    )

vectorstore=Chroma(
    collection_name="writer_memory",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

def retrieve_context(query, k=3):
    results = vectorstore.similarity_search(
        query,
        k=k
    )

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    return context