import ast
import warnings
from pathlib import Path


class SymbolIndexer:

    def __init__(self):
        self.index = {}

    def build(self, repository: str | Path):

        repository = Path(repository)

        warnings.filterwarnings("ignore", category=SyntaxWarning)

        for file in repository.rglob("*.py"):

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(
                    source,
                    filename=str(file),
                )

            except (SyntaxError, UnicodeDecodeError):
                continue

            except Exception:
                continue

            relative = file.relative_to(repository)

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):

                    self.index.setdefault(node.name, []).append(
                        {
                            "type": "class",
                            "file": str(relative),
                            "line": node.lineno,
                        }
                    )

                elif isinstance(
                    node,
                    (
                        ast.FunctionDef,
                        ast.AsyncFunctionDef,
                    ),
                ):

                    self.index.setdefault(node.name, []).append(
                        {
                            "type": "function",
                            "file": str(relative),
                            "line": node.lineno,
                        }
                    )

        return self.index

    def find(self, symbol: str):

        return self.index.get(symbol, [])