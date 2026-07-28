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


def ask_question(question):

    retriever = get_retriever()

    documents = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = f"""
You are an experienced DevOps Engineer.

Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    llm = OllamaLLM(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_HOST
    )

    response = llm.invoke(prompt)

    return response


if __name__ == "__main__":

    question = input(
        "Ask your DevOps question: "
    )

    answer = ask_question(question)

    print("\nAnswer:")
    print(answer)
