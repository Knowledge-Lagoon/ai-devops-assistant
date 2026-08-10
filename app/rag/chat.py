from langchain_chroma import Chroma
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


def ask_with_rag(
    request: str,
    retrieval_query: str | None = None
) -> str:

    retriever = get_retriever()

    query = (
    retrieval_query
    if retrieval_query
    else request
)

    documents = retriever.invoke(query)

#    print("\n=== QUERY SENT TO RAG ===\n")
#    print(request)

#    print("\n=== RETRIEVAL DEBUG ===\n")

#    for i, doc in enumerate(documents, start=1):

#        print(f"Result {i}")

#        print(doc.metadata)

#        print()

#        print(doc.page_content[:300])

#        print("\n" + "=" * 80 + "\n")

#    print("\n=== RETRIEVED DOCUMENTS ===\n")

#    for doc in documents:
#        print(doc.metadata)

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

#    print("\n=== RETRIEVED CONTENT ===\n")

#    for doc in documents:

#        print(
#            doc.page_content[:500]
#       )

#        print(
#            "\n" + "=" * 80 + "\n"
#       )

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