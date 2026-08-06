from pathlib import Path

from services.repo_loader import load_repository
from services.parser import parse_repository
from services.vectorstore import build_vectorstore


class RepositoryRetriever:

    def __init__(self, path: str | Path = "."):

        self.path = Path(path)

        files = load_repository(self.path)

        documents = parse_repository(files)

        # Each repository has its own FAISS index
        index_dir = self.path / ".devmind_index"

        self.vectorstore = build_vectorstore(
            documents,
            index_dir,
        )

    def search(self, query: str, k: int = 5):

        docs = self.vectorstore.similarity_search(
            query,
            k=k,
        )

        if not docs:
            return "No relevant repository context found."

        context = []

        for doc in docs:

            context.append(
                f"""
==================================================
FILE: {doc.metadata.get("source")}

{doc.page_content}
"""
            )

        return "\n".join(context)