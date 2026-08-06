from pathlib import Path
from langchain_core.documents import Document

SUPPORTED_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
}


def parse_repository(files: list[str]) -> list[Document]:
    """
    Convert repository files into LangChain Documents.
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

            documents.append(
                Document(
                    page_content=content,
                    metadata={
                        "source": str(path),
                        "file_name": path.name,
                        "extension": path.suffix,
                    },
                )
            )

        except Exception:
            continue

    return documents