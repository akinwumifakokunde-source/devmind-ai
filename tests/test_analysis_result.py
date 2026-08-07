from services.models.analysis_result import AnalysisResult


result = AnalysisResult(
    title="Repository Health",
    score=95,
    summary="Repository is well structured.",
    strengths=[
        "No circular dependencies",
        "Clear architecture",
    ],
    warnings=[
        "Large parser module",
    ],
    recommendations=[
        "Split parser.py",
        "Increase documentation",
    ],
)

print(result.to_markdown())