from services.graph.repository_graph_builder import (
    RepositoryGraphBuilder,
)

builder = RepositoryGraphBuilder(
    "repositories/langgraph"
)

graph = builder.build()

print("=" * 60)
print("Repository Graph")
print("=" * 60)

print()

print("Modules:", len(graph.modules))

print()

count = 0

for module in graph.modules.values():

    print(module.name)

    print("Internal :", len(module.internal))

    print("External :", len(module.external))

    print()

    count += 1

    if count == 10:
        break