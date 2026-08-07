import ast
from pathlib import Path
from collections import defaultdict


IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".devmind_index",
}


class DependencyGraph:

    def __init__(self, repository):

        self.repository = Path(repository)

        self.graph = defaultdict(set)

    def build(self):

        self.graph.clear()

        for file in self.repository.rglob("*.py"):

            if any(
                part in IGNORE_DIRS
                for part in file.parts
            ):
                continue

            relative = (
                file.relative_to(self.repository)
                .as_posix()
            )

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

            except Exception:
                continue

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for alias in node.names:

                        self.graph[relative].add(
                            alias.name
                        )

                elif isinstance(node, ast.ImportFrom):

                    if node.module:

                        self.graph[relative].add(
                            node.module
                        )

        return {
            key: sorted(value)
            for key, value in self.graph.items()
        }