from services.graph.circular_dependency_detector import (
    CircularDependencyDetector,
)
from services.graph.impact_analyzer import ImpactAnalyzer
from services.graph.graph_queries import GraphQueries


class RepositoryHealthAnalyzer:
    """
    Generates an engineering health report from the RepositoryGraph.
    """

    def __init__(self, graph):

        self.graph = graph
        self.queries = GraphQueries(graph)
        self.impact = ImpactAnalyzer(graph)
        self.cycles = CircularDependencyDetector(graph)

    def analyze(self):

        modules = len(self.graph.modules)

        imports = sum(
            len(node.internal)
            for node in self.graph.modules.values()
        )

        cycles = self.cycles.detect()

        average = 0

        if modules:

            average = imports / modules

        # ------------------------
        # Score
        # ------------------------

        score = 100

        score -= len(cycles) * 10

        if average > 15:
            score -= 15

        elif average > 10:
            score -= 10

        elif average > 5:
            score -= 5

        score = max(score, 0)

        return {
            "score": score,
            "modules": modules,
            "dependencies": imports,
            "dependency_cycles": len(cycles),
            "average_dependencies": round(
                average,
                2,
            ),
            "architecture": self.grade(score),
        }

    @staticmethod
    def grade(score):

        if score >= 90:
            return "Excellent"

        if score >= 80:
            return "Good"

        if score >= 70:
            return "Fair"

        return "Needs Improvement"