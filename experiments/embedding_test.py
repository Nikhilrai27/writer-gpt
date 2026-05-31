from dotenv import load_dotenv
import os

load_dotenv()

from langchain_huggingface import HuggingFaceEndpointEmbeddings

embeddings = HuggingFaceEndpointEmbeddings(
    model="BAAI/bge-small-en-v1.5",
    huggingfacehub_api_token=os.getenv(
        "HUGGINGFACEHUB_API_TOKEN"
    )
)

vector = embeddings.embed_query(
    "John is a detective who fears water"
)

print(type(vector))
print(len(vector))
print(vector[:5])