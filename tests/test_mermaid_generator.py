from services.graph.graph_models import RepositoryGraph
from services.graph.mermaid_generator import MermaidGenerator


graph = RepositoryGraph()

retriever = graph.add_module(
    "services/retriever.py"
)

retriever.imports.update(
    {
        "services.vectorstore",
        "services.parser",
    }
)

chat = graph.add_module(
    "services/chat_session.py"
)

chat.imports.add(
    "services/retriever.py"
)

generator = MermaidGenerator(graph)

print()
print("=" * 60)
print("Mermaid Diagram")
print("=" * 60)
print()

print(generator.generate())