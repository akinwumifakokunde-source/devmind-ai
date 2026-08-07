from services.graph.graph_models import RepositoryGraph


class CircularDependencyDetector:
    """
    Detect circular dependencies in a RepositoryGraph.
    """

    def __init__(self, graph: RepositoryGraph):

        self.graph = graph

        self.cycles = []

    def detect(self):

        self.cycles.clear()

        visited = set()

        stack = []

        def dfs(module):

            if module in stack:

                start = stack.index(module)

                cycle = stack[start:] + [module]

                if cycle not in self.cycles:
                    self.cycles.append(cycle)

                return

            if module in visited:
                return

            visited.add(module)

            stack.append(module)

            node = self.graph.module(module)

            if node:

                for dependency in node.internal:

                    dfs(dependency)

            stack.pop()

        for module in self.graph.modules:

            dfs(module)

        return self.cycles