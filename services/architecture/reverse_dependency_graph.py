from collections import defaultdict


class ReverseDependencyGraph:

    def __init__(self, dependency_graph):

        self.graph = dependency_graph

    def build(self):

        reverse = defaultdict(set)

        for source, imports in self.graph.items():

            for imported in imports:

                reverse[imported].add(source)

        return {
            key: sorted(value)
            for key, value in reverse.items()
        }