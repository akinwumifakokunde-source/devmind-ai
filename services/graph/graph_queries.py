from services.graph.graph_models import RepositoryGraph


class GraphQueries:
    """
    Query helper for RepositoryGraph.
    """

    def __init__(self, graph: RepositoryGraph):

        self.graph = graph

    # ---------------------------------------------------------
    # Check if a module exists
    # ---------------------------------------------------------

    def exists(self, module: str) -> bool:

        return module in self.graph.modules

    # ---------------------------------------------------------
    # Get one module
    # ---------------------------------------------------------

    def get(self, module: str):

        return self.graph.module(module)

    # ---------------------------------------------------------
    # Direct imports
    # ---------------------------------------------------------

    def upstream(self, module: str):

        node = self.graph.module(module)

        if node is None:
            return []

        return sorted(node.imports)

    # ---------------------------------------------------------
    # Reverse imports
    # ---------------------------------------------------------

    def downstream(self, module: str):

        result = []

        for node in self.graph.modules.values():

            if module in node.imports:
                result.append(node.name)

        return sorted(result)

    # ---------------------------------------------------------
    # Complete neighborhood
    # ---------------------------------------------------------

    def neighbors(self, module: str):

        return {
            "imports": self.upstream(module),
            "imported_by": self.downstream(module),
        }

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def statistics(self):

        total_imports = sum(
            len(node.imports)
            for node in self.graph.modules.values()
        )

        return {
            "modules": len(self.graph.modules),
            "imports": total_imports,
        }