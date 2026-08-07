from services.architecture.repository_health import (
    RepositoryHealthAnalyzer,
)
from services.graph.repository_graph_builder import (
    RepositoryGraphBuilder,
)
from services.review.code_reviewer import (
    CodeReviewer,
)


class RepositoryAudit:

    def __init__(self, repository):

        self.repository = repository

    def run(self):

        # Build graph from repository
        graph = RepositoryGraphBuilder(
            self.repository
        ).build()

        # Repository health
        health = RepositoryHealthAnalyzer(
            graph
        ).analyze()

        # AI review (replace with dynamic selection later)
        review = CodeReviewer().review(
            "services/retriever.py"
        )

        return {
            "health": health,
            "review": review,
        }