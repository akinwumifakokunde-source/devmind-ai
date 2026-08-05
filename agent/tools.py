from pathlib import Path
from langchain_core.tools import tool
from services.repository_scanner import RepositoryScanner


IGNORE_DIRS = {
    ".venv",
    ".git",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
    ".idea",
    ".vscode",
}

IGNORE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".pyd",
}


@tool
def list_files(directory: str = ".") -> str:
    """
    List project files while ignoring virtual environments,
    cache folders and IDE files.
    """

    root = Path(directory)

    if not root.exists():
        return "Directory not found."

    files = []

    for path in root.rglob("*"):

        # Skip ignored folders
        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        # Skip compiled files
        if path.suffix in IGNORE_SUFFIXES:
            continue

        if path.is_file():
            files.append(str(path.relative_to(root)))

    return "\n".join(sorted(files))


@tool
def read_file(file_path: str) -> str:
    """
    Read the contents of a text file.
    """

    path = Path(file_path)

    if not path.exists():
        return f"File not found: {file_path}"

    try:
        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    except Exception as e:
        return f"Error reading file: {e}"



@tool
def scan_repository() -> str:
    """
    Scan the current repository.
    """

    scanner = RepositoryScanner()

    return str(scanner.summary())