from pathlib import Path

from services.repo_loader import load_repository
from services.parser import parse_repository
from services.vectorstore import build_vectorstore


MAX_CONTEXT_CHARS = 8000


class RepositoryRetriever:

    def __init__(self, path: str | Path = "."):

        self.path = Path(path).resolve()

        files = load_repository(self.path)

        documents = parse_repository(files)

        index_dir = self.path / ".devmind_index"

        self.vectorstore = build_vectorstore(
            documents,
            index_dir,
        )

    def search(self, query: str, k: int = 4) -> dict:

        results = self.vectorstore.similarity_search_with_score(
            query,
            k=k,
        )

        if not results:
            return {
                "context": "No relevant repository context found.",
                "sources": [],
            }

        context = []
        sources = []
        current_size = 0

        for doc, score in results:

            text = doc.page_content

            if current_size + len(text) > MAX_CONTEXT_CHARS:
                break

            current_size += len(text)

            source = Path(doc.metadata.get("source", ""))

            try:
                relative = source.resolve().relative_to(self.path)
            except Exception:
                relative = source.name

            relative = str(relative).replace("\\", "/")

            chunk = doc.metadata.get("chunk", 1)

            if relative not in sources:
                sources.append(relative)

            context.append(
                f"""
==================================================
FILE: {relative}
CHUNK: {chunk}

{text}
"""
            )

        return {
            "context": "\n".join(context),
            "sources": sources,
        }