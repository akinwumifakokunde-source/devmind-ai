from services.graph.graph_models import RepositoryGraph
from services.graph.graph_queries import GraphQueries


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

queries = GraphQueries(graph)

print("=" * 60)
print("Graph Queries")
print("=" * 60)

print()

print("Exists")
print(
    queries.exists(
        "services/retriever.py"
    )
)

print()

print("Upstream")
print(
    queries.upstream(
        "services/retriever.py"
    )
)

print()

print("Downstream")
print(
    queries.downstream(
        "services/retriever.py"
    )
)

print()

print("Neighbors")
print(
    queries.neighbors(
        "services/retriever.py"
    )
)

print()

print("Statistics")
print(
    queries.statistics()
)