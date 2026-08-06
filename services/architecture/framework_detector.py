from pathlib import Path


FRAMEWORKS = {
    "LangChain": [
        "langchain",
    ],
    "LangGraph": [
        "langgraph",
    ],
    "FastAPI": [
        "fastapi",
    ],
    "Flask": [
        "flask",
    ],
    "Django": [
        "django",
    ],
    "Streamlit": [
        "streamlit",
    ],
    "Gradio": [
        "gradio",
    ],
    "OpenAI": [
        "openai",
    ],
    "Anthropic": [
        "anthropic",
    ],
    "Groq": [
        "groq",
    ],
    "FAISS": [
        "faiss",
    ],
    "Chroma": [
        "chromadb",
        "chroma",
    ],
    "Pinecone": [
        "pinecone",
    ],
    "Milvus": [
        "milvus",
    ],
    "Redis": [
        "redis",
    ],
    "Celery": [
        "celery",
    ],
    "SQLAlchemy": [
        "sqlalchemy",
    ],
    "PostgreSQL": [
        "psycopg",
        "postgres",
    ],
    "PyTorch": [
        "torch",
    ],
    "TensorFlow": [
        "tensorflow",
    ],
    "NumPy": [
        "numpy",
    ],
    "Pandas": [
        "pandas",
    ],
    "Pytest": [
        "pytest",
    ],
}


class FrameworkDetector:

    def __init__(self, repository):

        self.repository = Path(repository)

    def detect(self):

        detected = set()

        for file in self.repository.rglob("*"):

            if not file.is_file():
                continue

            if file.suffix not in {
                ".py",
                ".toml",
                ".txt",
                ".yaml",
                ".yml",
                ".md",
                ".json",
            }:
                continue

            try:

                text = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                ).lower()

            except Exception:
                continue

            for framework, keywords in FRAMEWORKS.items():

                if any(keyword in text for keyword in keywords):
                    detected.add(framework)

        return sorted(detected)