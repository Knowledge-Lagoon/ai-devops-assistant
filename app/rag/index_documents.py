from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents
from app.rag.embeddings import get_embeddings
from app.rag.vector_store import create_vector_store


def main():

    documents = load_documents(
       "documents"
)

    chunks = split_documents(
        documents
    )

    embeddings = get_embeddings()

    create_vector_store(
        chunks,
        embeddings
    )

    print("Documents indexed successfully")


if __name__ == "__main__":
    main()
