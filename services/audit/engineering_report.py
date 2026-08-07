from services.models.analysis_result import (
    AnalysisResult,
)


class EngineeringReport:

    def generate(
        self,
        health,
        architecture,
    ) -> AnalysisResult:

        strengths = []

        recommendations = []

        score = health["score"]

        if health["dependency_cycles"] == 0:

            strengths.append(
                "No circular dependencies detected."
            )

        if score > 90:

            strengths.append(
                "Repository architecture is well organized."
            )

        if health["average_dependencies"] > 10:

            recommendations.append(
                "Reduce coupling between modules."
            )

        return AnalysisResult(
            title="Engineering Report",
            score=score,
            summary=(
                "Overall repository engineering analysis."
            ),
            strengths=strengths,
            recommendations=recommendations,
            metadata={
                "health": health,
                "architecture": architecture,
            },
        )