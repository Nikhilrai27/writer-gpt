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