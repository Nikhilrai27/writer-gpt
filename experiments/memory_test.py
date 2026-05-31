from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

embeddings=GoogleGenerativeAIEmbeddings(
    model="models/embedding-001")

vectorstore = Chroma(
    collection_name="characters",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

vectorstore.add_texts(
    [
        """
        John is a 34-year-old detective.
        He fears water.
        He works in Chicago.
        """
    ]
)
print("Character stored.")