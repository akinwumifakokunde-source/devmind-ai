from pathlib import Path

from services.repository_scanner import RepositoryScanner


def load_repository(path="."):
    """
    Load all repository files from the specified path.

    Args:
        path (str | Path): Repository root directory.

    Returns:
        list[str]: List of repository file paths.
    """

    scanner = RepositoryScanner(Path(path))

    files = scanner.scan()

    return [str(file) for file in files]