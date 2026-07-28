from pathlib import Path

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader
)


def load_documents(folder_path):

    documents = []

    folder = Path(folder_path)

    for file in folder.rglob("*"):

        if file.suffix == ".txt":
            loader = TextLoader(
                str(file),
                encoding="utf-8"
            )

        elif file.suffix == ".pdf":
            loader = PyPDFLoader(
                str(file)
            )

        elif file.suffix == ".docx":
            loader = Docx2txtLoader(
                str(file)
            )

        else:
            continue

        docs = loader.load()

        for doc in docs:
            doc.metadata["file_name"] = file.name
            doc.metadata["source"] = str(file)

        documents.extend(docs)

    return documents