from pathlib import Path

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from services.llm import get_llm
from services.retriever import RepositoryRetriever
from services.symbol_explainer import SymbolExplainer
from services.symbol_index import SymbolIndexer


llm = get_llm()

# Repository-specific services (initialized later)
retriever = None
symbol_index = None
symbol_explainer = None


def initialize_tools(repository_path):
    """
    Initialize repository-specific services after a repository
    has been cloned and indexed.
    """
    global retriever
    global symbol_index
    global symbol_explainer

    retriever = RepositoryRetriever(repository_path)

    symbol_index = SymbolIndexer()
    symbol_index.build(repository_path)

    symbol_explainer = SymbolExplainer(repository_path)


IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".idea",
    ".vscode",
    ".devmind_index",
}


# ------------------------------------------------------------------
# List Files
# ------------------------------------------------------------------

@tool
def list_files(directory: str = ".") -> str:
    """
    List every project file.
    """

    root = Path(directory)

    files = []

    for path in root.rglob("*"):

        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        if path.is_file():
            files.append(str(path.relative_to(root)))

    if not files:
        return "No files found."

    return "\n".join(sorted(files))


# ------------------------------------------------------------------
# Read File
# ------------------------------------------------------------------

@tool
def read_file(path: str) -> str:
    """
    Read a repository file.
    """

    try:

        return Path(path).read_text(
            encoding="utf-8",
            errors="ignore",
        )

    except Exception as e:
        return f"Error reading file: {e}"


# ------------------------------------------------------------------
# Semantic Search
# ------------------------------------------------------------------

@tool
def search_repository(query: str) -> dict:
    """
    Search the repository semantically.
    """

    if retriever is None:
        return {
            "context": "Repository has not been initialized.",
            "sources": [],
        }

    return retriever.search(query)


# ------------------------------------------------------------------
# Explain File
# ------------------------------------------------------------------

@tool
def explain_file(path: str) -> str:
    """
    Explain an entire source file.
    """

    try:

        content = Path(path).read_text(
            encoding="utf-8",
            errors="ignore",
        )

    except Exception as e:
        return f"Error reading file: {e}"

    prompt = f"""
You are DevMind AI.

You are an expert software engineer.

Analyze this source code.

Return:

# Purpose

# Classes

# Functions

# Dependencies

# Workflow

# Improvements

Rules

- Do not rewrite the code.
- Do not copy large sections.
- Be concise.
- Explain like a senior engineer.

Source Code
===========

{content}
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return response.content


# ------------------------------------------------------------------
# Find Symbol
# ------------------------------------------------------------------

@tool
def find_symbol(name: str) -> str:
    """
    Find where a class, function or method is defined.
    """

    if symbol_index is None:
        return "Repository has not been initialized."

    results = symbol_index.find(name)

    if not results:
        return f"No symbol named '{name}' found."

    lines = [
        "=" * 60,
        f"Symbol: {name}",
        "=" * 60,
        "",
    ]

    for i, result in enumerate(results, start=1):

        lines.extend(
            [
                f"Match {i}",
                f"Type : {result['type']}",
                f"File : {result['file']}",
                f"Line : {result['line']}",
                "-" * 60,
            ]
        )

    return "\n".join(lines)


# ------------------------------------------------------------------
# Explain Symbol
# ------------------------------------------------------------------

@tool
def explain_symbol(name: str) -> str:
    """
    Explain a class, function or method.
    """

    if symbol_explainer is None:
        return "Repository has not been initialized."

    return symbol_explainer.explain(name)


# ------------------------------------------------------------------
# Registered Tools
# ------------------------------------------------------------------

tools = [
    list_files,
    read_file,
    search_repository,
    explain_file,
    find_symbol,
    explain_symbol,
]