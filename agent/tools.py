from pathlib import Path

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from services.llm import get_llm
from services.retriever import RepositoryRetriever

retriever = RepositoryRetriever()
llm = get_llm()

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".idea",
    ".vscode",
}


@tool
def list_files(directory: str = ".") -> str:
    """
    List all project files while ignoring cache folders.
    """

    root = Path(directory)

    files = []

    for path in root.rglob("*"):

        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        if path.is_file():
            files.append(str(path))

    return "\n".join(sorted(files))


@tool
def read_file(path: str) -> str:
    """
    Read a file from the repository.
    """

    try:
        return Path(path).read_text(
            encoding="utf-8",
            errors="ignore",
        )

    except Exception as e:
        return f"Error reading file: {e}"


@tool
def search_repository(query: str) -> str:
    """
    Perform semantic search over the repository.
    """

    return retriever.search(query)


@tool
def explain_file(path: str) -> str:
    """
    Read a repository file and generate a professional explanation.
    """

    try:
        content = Path(path).read_text(
            encoding="utf-8",
            errors="ignore",
        )

    except Exception as e:
        return f"Error reading file: {e}"

    prompt = f"""
You are DevMind AI, an expert software engineer.

Analyze the following source code.

Return your answer using exactly this format.

# Purpose

A short summary.

# Classes

List every class and explain its responsibility.

# Functions

List every function and explain what it does.

# Dependencies

Explain imported libraries and modules.

# Workflow

Explain the execution flow from start to finish.

# Improvements

Suggest improvements following Python best practices.

Rules:
- Do NOT rewrite the source code.
- Do NOT copy large portions of the code.
- Explain the architecture and design.
- Keep the explanation concise and professional.

Source Code
-----------

{content}
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return response.content


tools = [
    list_files,
    read_file,
    search_repository,
    explain_file,
]