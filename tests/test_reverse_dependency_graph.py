from pprint import pprint

from services.architecture.dependency_graph import DependencyGraph
from services.architecture.reverse_dependency_graph import (
    ReverseDependencyGraph,
)

graph = DependencyGraph(
    "repositories/langgraph"
).build()

reverse = ReverseDependencyGraph(
    graph
).build()

print()

print("=" * 60)
print("Reverse Dependency Graph")
print("=" * 60)

count = 0

for module, imported_by in reverse.items():

    pprint(
        {
            module: imported_by
        }
    )

    count += 1

    if count == 10:
        break