from pathlib import Path


ENTRYPOINT_NAMES = {
    "main.py",
    "__main__.py",
    "app.py",
    "server.py",
    "run.py",
    "manage.py",
    "cli.py",
}


IGNORE_PARTS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".devmind_index",
}


IGNORE_PATHS = {
    "tests",
    "test",
    "bench",
    "benchmark",
    "benchmarks",
    "examples",
    "example",
    "scripts",
    "integration",
}


class EntrypointDetector:

    def __init__(self, repository):

        self.repository = Path(repository)

    def _should_ignore(self, path: Path):

        for part in path.parts:

            part = part.lower()

            if part in IGNORE_PARTS:
                return True

            if part in IGNORE_PATHS:
                return True

        return False

    def detect(self):

        entrypoints = []

        for file in self.repository.rglob("*.py"):

            if self._should_ignore(file):
                continue

            relative = file.relative_to(
                self.repository
            ).as_posix()

            if file.name.lower() in ENTRYPOINT_NAMES:

                entrypoints.append(relative)
                continue

            try:

                text = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

            except Exception:
                continue

            startup_patterns = (
                "uvicorn.run(",
                "app.run(",
                "FastAPI(",
                "Flask(",
                "typer.Typer(",
                "click.command(",
                "argparse.ArgumentParser(",
            )

            if (
                "__name__" in text
                and any(
                    pattern in text
                    for pattern in startup_patterns
                )
            ):
                entrypoints.append(relative)

        return sorted(set(entrypoints))