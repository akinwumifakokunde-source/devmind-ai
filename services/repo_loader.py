from pathlib import Path

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".idea",
    ".vscode",
    ".mypy_cache",
}


def load_repository(root: str = ".") -> list[str]:
    """
    Return all files in the repository while ignoring
    virtual environments, Git folders, caches, etc.
    """

    files = []

    for path in Path(root).rglob("*"):

        if not path.is_file():
            continue

        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        files.append(str(path))

    return files