from pprint import pprint

from services.architecture.dependency_graph import (
    DependencyGraph,
)

graph = DependencyGraph(
    "repositories/langgraph"
)

result = graph.build()

print()
print("=" * 60)
print("Dependency Graph")
print("=" * 60)

count = 0

for module, imports in result.items():

    pprint(
        {
            module: imports
        }
    )

    count += 1

    if count == 10:
        break