from pathlib import Path


def read_around_line(
    repository: str | Path,
    file: str,
    line: int,
    before: int = 40,
    after: int = 80,
) -> str:
    """
    Read a section of a file around a given line.
    """

    path = Path(repository) / file

    lines = path.read_text(
        encoding="utf-8",
        errors="ignore",
    ).splitlines()

    start = max(0, line - before - 1)
    end = min(len(lines), line + after)

    output = []

    for i in range(start, end):

        output.append(
            f"{i + 1:4}: {lines[i]}"
        )

    return "\n".join(output)