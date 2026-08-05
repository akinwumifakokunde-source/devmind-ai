from pathlib import Path


IGNORE_DIRS = {
    ".venv",
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".idea",
    ".vscode",
    "node_modules",
}


class RepositoryScanner:

    def __init__(self, root="."):
        self.root = Path(root)

    def scan(self):

        files = []

        for path in self.root.rglob("*"):

            if any(part in IGNORE_DIRS for part in path.parts):
                continue

            if path.is_file():
                files.append(path)

        return files

    def summary(self):

        files = self.scan()

        python_files = [f for f in files if f.suffix == ".py"]

        frameworks = []

        text = ""

        for file in python_files:

            try:
                text += file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

            except:
                pass

        if "langchain" in text.lower():
            frameworks.append("LangChain")

        if "langgraph" in text.lower():
            frameworks.append("LangGraph")

        if "streamlit" in text.lower():
            frameworks.append("Streamlit")

        if "fastapi" in text.lower():
            frameworks.append("FastAPI")

        if "ChatGroq" in text:
            frameworks.append("Groq")

        return {
            "project": self.root.name,
            "python_files": len(python_files),
            "frameworks": frameworks,
            "files": len(files),
        }