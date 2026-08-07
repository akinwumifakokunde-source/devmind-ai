from services.graph.graph_models import RepositoryGraph


class MermaidGenerator:
    """
    Generates Mermaid diagrams from a RepositoryGraph.
    """

    def __init__(self, graph: RepositoryGraph):
        self.graph = graph

    @staticmethod
    def _clean(name: str) -> str:
        return (
            name.replace("/", "_")
                .replace("\\", "_")
                .replace(".", "_")
                .replace("-", "_")
        )

    def generate(self) -> str:

        lines = [
            "graph TD",
            ""
        ]

        for module in self.graph.modules.values():

            source = self._clean(module.name)

            for dependency in sorted(module.imports):

                target = self._clean(dependency)

                lines.append(
                    f'    {source} --> {target}'
                )

        return "\n".join(lines)