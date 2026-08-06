import subprocess
from pathlib import Path

REPOSITORIES = Path("repositories")
REPOSITORIES.mkdir(exist_ok=True)


def clone_repository(url: str) -> Path:
    """
    Clone a GitHub repository if it doesn't already exist.
    If it already exists, reuse it.
    """

    repo_name = url.rstrip("/").split("/")[-1].replace(".git", "")

    destination = REPOSITORIES / repo_name

    # Reuse existing clone
    if destination.exists():
        print(f"Using existing repository: {destination}")
        return destination

    print(f"Cloning {url}...")

    subprocess.run(
        [
            "git",
            "clone",
            url,
            str(destination),
        ],
        check=True,
    )

    return destination