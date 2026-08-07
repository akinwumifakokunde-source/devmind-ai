from collections import deque

from services.graph.graph_models import RepositoryGraph
from services.graph.graph_queries import GraphQueries


class ImpactAnalyzer:
    """
    Analyze the impact of modifying a module.
    """

    def __init__(self, graph: RepositoryGraph):

        self.graph = graph
        self.queries = GraphQueries(graph)

    def analyze(self, module: str):

        if not self.queries.exists(module):

            return {
                "module": module,
                "risk": "Unknown",
                "direct": [],
                "indirect": [],
                "total": 0,
            }

        # ------------------------------------------
        # Direct dependents
        # ------------------------------------------

        direct = set(
            self.queries.downstream(module)
        )

        # ------------------------------------------
        # Indirect dependents (BFS)
        # ------------------------------------------

        visited = set(direct)

        queue = deque(direct)

        indirect = set()

        while queue:

            current = queue.popleft()

            for nxt in self.queries.downstream(current):

                if nxt not in visited:

                    visited.add(nxt)

                    indirect.add(nxt)

                    queue.append(nxt)

        total = len(direct) + len(indirect)

        # ------------------------------------------
        # Risk score
        # ------------------------------------------

        if total >= 20:

            risk = "Critical"

        elif total >= 10:

            risk = "High"

        elif total >= 5:

            risk = "Medium"

        else:

            risk = "Low"

        return {
            "module": module,
            "risk": risk,
            "direct": sorted(direct),
            "indirect": sorted(indirect),
            "total": total,
        }