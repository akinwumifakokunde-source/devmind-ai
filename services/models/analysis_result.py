from dataclasses import dataclass, field


@dataclass
class AnalysisResult:
    """
    Standard result returned by every DevMind analyzer.
    """

    title: str

    score: int | None = None

    summary: str = ""

    strengths: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    def to_markdown(self) -> str:

        lines = [
            f"# {self.title}",
            "",
        ]

        if self.score is not None:

            lines.extend([
                f"## Score",
                "",
                str(self.score),
                "",
            ])

        if self.summary:

            lines.extend([
                "## Summary",
                "",
                self.summary,
                "",
            ])

        if self.strengths:

            lines.append("## Strengths")
            lines.append("")

            for item in self.strengths:
                lines.append(f"- {item}")

            lines.append("")

        if self.warnings:

            lines.append("## Warnings")
            lines.append("")

            for item in self.warnings:
                lines.append(f"- {item}")

            lines.append("")

        if self.recommendations:

            lines.append("## Recommendations")
            lines.append("")

            for item in self.recommendations:
                lines.append(f"- {item}")

            lines.append("")

        return "\n".join(lines)