from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


SUPPORTED_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
}


splitter = RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=100,
)


def parse_repository(files: list[str]) -> list[Document]:
    """
    Parse repository files into chunked LangChain documents.
    """

    documents = []

    for file in files:

        path = Path(file)

        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        try:

            content = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            metadata = {
                "source": str(path),
                "file_name": path.name,
                "extension": path.suffix,
            }

            chunks = splitter.create_documents(
                [content],
                metadatas=[metadata],
            )

            for i, chunk in enumerate(chunks):
                chunk.metadata["chunk"] = i + 1

            documents.extend(chunks)

        except Exception:
            continue

    return documents