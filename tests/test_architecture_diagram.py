from services.graph.graph_models import RepositoryGraph
from services.graph.architecture_diagram import ArchitectureDiagram


graph = RepositoryGraph()

chat = graph.add_module(
    "services/chat_session.py"
)

retriever = graph.add_module(
    "services/retriever.py"
)

parser = graph.add_module(
    "services/parser.py"
)

agent = graph.add_module(
    "agent/tools.py"
)

chat.imports.add(
    "services/retriever.py"
)

retriever.imports.add(
    "services/parser.py"
)

agent.imports.add(
    "services/retriever.py"
)

diagram = ArchitectureDiagram(graph)

print("=" * 60)
print("Architecture Diagram")
print("=" * 60)
print()

print(diagram.generate())