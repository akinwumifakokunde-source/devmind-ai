from agent.final_answer import generate_final_answer
from agent.tools import (
    initialize_tools,
    explain_file,
    explain_symbol,
    find_symbol,
    list_files,
    read_file,
)
from services.project_analyzer import ProjectAnalyzer


class ChatSession:

    def __init__(self, github_url: str):

        analyzer = ProjectAnalyzer()

        self.retriever = analyzer.analyze(github_url)

        # Initialize all repository-specific tools
        initialize_tools(self.retriever.path)

    def ask(self, question: str) -> str:

        q = question.strip()
        lower = q.lower()

        # ---------------------------------------------------------
        # Explain a source file
        # ---------------------------------------------------------

        if lower.startswith("explain ") and q.endswith(".py"):

            path = q[len("Explain "):].strip()

            return explain_file.invoke(
                {
                    "path": path
                }
            )

        # ---------------------------------------------------------
        # Explain a symbol
        # ---------------------------------------------------------

        if lower.startswith("explain "):

            symbol = (
                q[len("Explain "):]
                .replace("()", "")
                .replace("?", "")
                .strip()
            )

            # Support: Explain StateGraph.compile()
            if "." in symbol:
                symbol = symbol.split(".")[-1]

            return explain_symbol.invoke(
                {
                    "name": symbol
                }
            )

        # ---------------------------------------------------------
        # Find symbol
        # ---------------------------------------------------------

        if lower.startswith("find symbol"):

            symbol = (
                q[len("Find symbol"):]
                .replace("?", "")
                .strip()
            )

            return find_symbol.invoke(
                {
                    "name": symbol
                }
            )

        if lower.startswith("where is"):

            symbol = (
                q[len("Where is"):]
                .replace("defined", "")
                .replace("located", "")
                .replace("?", "")
                .strip()
            )

            if "." in symbol:
                symbol = symbol.split(".")[-1]

            return find_symbol.invoke(
                {
                    "name": symbol
                }
            )

        # ---------------------------------------------------------
        # Read a file
        # ---------------------------------------------------------

        if lower.startswith("read "):

            path = q[len("Read "):].strip()

            return read_file.invoke(
                {
                    "path": path
                }
            )

        # ---------------------------------------------------------
        # List project files
        # ---------------------------------------------------------

        if lower in {
            "list files",
            "show files",
            "show project files",
        }:

            return list_files.invoke(
                {
                    "directory": str(self.retriever.path)
                }
            )

        # ---------------------------------------------------------
        # Default: semantic repository search
        # ---------------------------------------------------------

        result = self.retriever.search(q)

        return generate_final_answer(
            question=q,
            tool_result=result,
        )