from pprint import pprint

from services.architecture.architecture_analyzer import (
    ArchitectureAnalyzer,
)

analyzer = ArchitectureAnalyzer(
    "repositories/langgraph"
)

summary = analyzer.analyze()

print()
print("=" * 60)
print("Architecture Summary")
print("=" * 60)

pprint(summary)