from pprint import pprint

from services.graph.graph_models import RepositoryGraph
from services.architecture.repository_health import (
    RepositoryHealthAnalyzer,
)

graph = RepositoryGraph()

A = graph.add_module("A.py")
B = graph.add_module("B.py")
C = graph.add_module("C.py")

B.internal.add("A.py")
C.internal.add("B.py")

health = RepositoryHealthAnalyzer(graph)

print()
print("=" * 60)
print("Repository Health")
print("=" * 60)

print()

pprint(
    health.analyze()
)