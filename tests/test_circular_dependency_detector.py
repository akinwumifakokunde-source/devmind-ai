from services.graph.graph_models import RepositoryGraph
from services.graph.circular_dependency_detector import (
    CircularDependencyDetector,
)


graph = RepositoryGraph()

a = graph.add_module("A.py")
b = graph.add_module("B.py")
c = graph.add_module("C.py")
d = graph.add_module("D.py")

a.internal.add("B.py")
b.internal.add("C.py")
c.internal.add("A.py")

d.internal.add("A.py")

detector = CircularDependencyDetector(graph)

cycles = detector.detect()

print()
print("=" * 60)
print("Circular Dependencies")
print("=" * 60)
print()

for cycle in cycles:

    print(" -> ".join(cycle))