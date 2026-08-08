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
        """
        Return modules that directly depend on the given module.

        Supports both repository paths and Python module names.

        Examples:
            services/retriever.py
            services.retriever
        """

        normalized = module.replace("\\", "/")

        if normalized.endswith(".py"):
            normalized = normalized[:-3]

        normalized = normalized.replace("/", ".")

        result = []

        for node in self.graph.modules.values():
            for imported in node.imports:
                imported_normalized = imported.replace("\\", "/")

                if imported_normalized.endswith(".py"):
                    imported_normalized = imported_normalized[:-3]

                imported_normalized = imported_normalized.replace(
                    "/", "."
                )

                if (
                    imported == module
                    or imported_normalized == normalized
                ):
                    result.append(node.name)
                    break

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
