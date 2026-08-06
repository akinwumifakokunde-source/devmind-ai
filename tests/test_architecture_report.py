from services.architecture.architecture_analyzer import (
    ArchitectureAnalyzer,
)
from services.architecture.architecture_report import (
    ArchitectureReportGenerator,
)

analyzer = ArchitectureAnalyzer(
    "repositories/langgraph"
)

summary = analyzer.analyze()

generator = ArchitectureReportGenerator()

report = generator.generate(summary)

print()
print("=" * 60)
print("Architecture Report")
print("=" * 60)
print()

print(report)