from langchain_community.vectorstores import Chroma

from app.config import OLLAMA_HOST


def create_vector_store(documents, embeddings):

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    return vector_store
