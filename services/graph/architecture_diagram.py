from pathlib import Path

from services.graph.graph_models import RepositoryGraph


class ArchitectureDiagram:
    """
    Generate a high-level Mermaid architecture diagram.
    """

    def __init__(self, graph: RepositoryGraph):

        self.graph = graph

    def _group(self, module: str) -> str:

        module = module.replace("\\", "/")

        if module.startswith("agent/"):
            return "Agent"

        if module.startswith("services/"):
            return "Services"

        if module.startswith("tests/"):
            return "Tests"

        if module.startswith("docs/"):
            return "Documentation"

        return "Other"

    def generate(self):

        groups = {}

        for module in self.graph.modules.values():

            group = self._group(module.name)

            groups.setdefault(group, []).append(module)

        lines = [
            "graph TD",
            "",
        ]

        # ------------------------------------------
        # Create groups
        # ------------------------------------------

        for group, modules in groups.items():

            lines.append(f"subgraph {group}")

            for module in sorted(modules, key=lambda x: x.name):

                node = (
                    Path(module.name)
                    .stem
                    .replace("-", "_")
                )

                lines.append(
                    f"    {node}[{node}]"
                )

            lines.append("end")
            lines.append("")

        # ------------------------------------------
        # Draw edges
        # ------------------------------------------

        for module in self.graph.modules.values():

            source = (
                Path(module.name)
                .stem
                .replace("-", "_")
            )

            for dependency in sorted(module.imports):

                target = (
                    Path(dependency)
                    .stem
                    .replace("-", "_")
                )

                lines.append(
                    f"{source} --> {target}"
                )

        return "\n".join(lines)