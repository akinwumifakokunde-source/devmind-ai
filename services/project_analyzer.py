from services.github import clone_repository
from services.retriever import RepositoryRetriever


class ProjectAnalyzer:

    def analyze(self, github_url: str):

        repo_path = clone_repository(github_url)

        return RepositoryRetriever(repo_path)