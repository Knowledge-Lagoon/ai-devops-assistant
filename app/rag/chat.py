from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM

from app.config import (
    OLLAMA_HOST,
    OLLAMA_MODEL,
    OLLAMA_EMBEDDING_MODEL
)


def get_retriever():

    embeddings = OllamaEmbeddings(
        model=OLLAMA_EMBEDDING_MODEL,
        base_url=OLLAMA_HOST
    )

    vector_db = Chroma(
        persist_directory="vector_db",
        embedding_function=embeddings
    )

    return vector_db.as_retriever(
        search_kwargs={
            "k": 3
        }
    )


def ask_with_rag(request: str) -> str:

    retriever = get_retriever()

    documents = retriever.invoke(request)

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = f"""
You are an experienced DevOps Engineer.

Use ONLY the provided context to answer the request.

Context:
{context}

Request:
{request}

Answer:
"""

    llm = OllamaLLM(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_HOST
    )

    response = llm.invoke(prompt)

    return response


def ask_question(question: str) -> str:
    """
    Backward compatibility with Project 2.
    """
    return ask_with_rag(question)


if __name__ == "__main__":

    question = input(
        "Ask your DevOps question: "
    )

    answer = ask_question(question)

    print("\nAnswer:")
    print(answer)