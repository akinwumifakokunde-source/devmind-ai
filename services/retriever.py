from agent.tools import list_files

from services.parser import parse_repository
from services.vectorstore import build_vectorstore


class RepositoryRetriever:

    def __init__(self):

        files = list_files.invoke({}).splitlines()

        documents = parse_repository(files)

        self.vectorstore = build_vectorstore(documents)

    def search(self, query: str, k: int = 5):

        return self.vectorstore.similarity_search(
            query,
            k=k,
        )