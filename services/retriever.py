from services.repo_loader import load_repository
from services.parser import parse_repository
from services.vectorstore import build_vectorstore


class RepositoryRetriever:

    def __init__(self):
        self.vectorstore = None

    def _load(self):
        if self.vectorstore is None:
            files = load_repository()
            documents = parse_repository(files)
            self.vectorstore = build_vectorstore(documents)

    def search(self, query: str, k: int = 5) -> str:

        self._load()

        docs = self.vectorstore.similarity_search(query, k=k)

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