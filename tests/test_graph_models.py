from services.graph.graph_models import RepositoryGraph

graph = RepositoryGraph()

graph.add_module(
    "services/retriever.py"
)

graph.add_module(
    "services/vectorstore.py"
)

print()

print("=" * 60)
print("Repository Graph")
print("=" * 60)

print()

print("Modules")

for module in graph.modules.values():

    print(module.name)