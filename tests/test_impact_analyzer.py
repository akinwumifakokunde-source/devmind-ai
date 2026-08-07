from pprint import pprint

from services.graph.graph_models import RepositoryGraph
from services.graph.impact_analyzer import ImpactAnalyzer


graph = RepositoryGraph()

# A -> B -> C -> D

a = graph.add_module("A.py")

b = graph.add_module("B.py")

c = graph.add_module("C.py")

d = graph.add_module("D.py")


b.imports.add("A.py")

c.imports.add("B.py")

d.imports.add("C.py")


impact = ImpactAnalyzer(graph)

result = impact.analyze("A.py")

print()
print("=" * 60)
print("Impact Analysis")
print("=" * 60)

pprint(result)