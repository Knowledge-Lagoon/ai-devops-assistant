import chromadb
from chromadb.config import Settings


class VectorStore:
    def __init__(
        self,
        persist_directory="vector_db",
        collection_name="devops_docs",
    ):
        self.client = chromadb.PersistentClient(path=persist_directory)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(self, chunks, embeddings, metadata=None):
        """
        Store document chunks and embeddings in ChromaDB.

        Parameters:
            chunks (list[str])
            embeddings (list[list[float]])
            metadata (list[dict]) optional
        """

        ids = [f"doc_{i}" for i in range(len(chunks))]

        if metadata is None:
            metadata = [{} for _ in chunks]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadata,
        )

    def count(self):
        return self.collection.count()