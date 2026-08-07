import ast
from pathlib import Path

from services.graph.graph_models import RepositoryGraph


IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".devmind_index",
}


class RepositoryGraphBuilder:
    """
    Builds a RepositoryGraph from an entire repository.
    """

    def __init__(self, repository):

        self.repository = Path(repository).resolve()

    def build(self):

        graph = RepositoryGraph()

        # -----------------------------------------------------
        # Pass 1 - Discover all Python modules
        # -----------------------------------------------------

        python_modules = set()

        for file in self.repository.rglob("*.py"):

            if any(
                part in IGNORE_DIRS
                for part in file.parts
            ):
                continue

            relative = file.relative_to(
                self.repository
            ).as_posix()

            python_modules.add(relative)

            graph.add_module(relative)

        # -----------------------------------------------------
        # Pass 2 - Parse imports
        # -----------------------------------------------------

        for file in self.repository.rglob("*.py"):

            if any(
                part in IGNORE_DIRS
                for part in file.parts
            ):
                continue

            relative = file.relative_to(
                self.repository
            ).as_posix()

            node = graph.module(relative)

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

            except Exception:

                continue

            for item in ast.walk(tree):

                # -----------------------------
                # import xxx
                # -----------------------------

                if isinstance(item, ast.Import):

                    for alias in item.names:

                        module = alias.name

                        node.imports.add(module)

                # -----------------------------
                # from xxx import ...
                # -----------------------------

                elif isinstance(item, ast.ImportFrom):

                    if item.module:

                        node.imports.add(
                            item.module
                        )

        # -----------------------------------------------------
        # Pass 3 - Classify imports
        # -----------------------------------------------------

        module_lookup = {}

        for module in python_modules:

            dotted = (
                module[:-3]
                .replace("/", ".")
            )

            module_lookup[dotted] = module

        for node in graph.modules.values():

            for imported in node.imports:

                matched = False

                for dotted, path in module_lookup.items():

                    if imported.startswith(dotted):

                        node.internal.add(path)

                        matched = True
                        break

                if not matched:

                    node.external.add(imported)

        return graph