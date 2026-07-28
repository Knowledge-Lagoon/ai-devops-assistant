from langchain_ollama import OllamaEmbeddings

from app.config import (
    OLLAMA_HOST,
    OLLAMA_EMBEDDING_MODEL,
)


def get_embeddings():

    return OllamaEmbeddings(
        model=OLLAMA_EMBEDDING_MODEL,
        base_url=OLLAMA_HOST,
    )
