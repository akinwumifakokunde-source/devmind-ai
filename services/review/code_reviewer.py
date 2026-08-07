from pathlib import Path

from langchain_core.messages import HumanMessage

from services.llm import get_llm
from services.models.analysis_result import AnalysisResult


class CodeReviewer:
    """
    AI-powered code reviewer.
    """

    def __init__(self):

        self.llm = get_llm()

    def review(self, file_path: str) -> AnalysisResult:

        path = Path(file_path)

        if not path.exists():

            return AnalysisResult(
                title="Code Review",
                score=0,
                summary=f"{file_path} does not exist.",
            )

        source = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        prompt = f"""
You are a Principal Software Engineer.

Review the following Python file.

Evaluate:

1. Correctness
2. Readability
3. Maintainability
4. Performance
5. Security
6. Error Handling
7. SOLID Principles
8. Testability

Return your answer in this EXACT format.

Score:
<0-100>

Summary:
<summary>

Strengths:
- ...

Warnings:
- ...

Recommendations:
- ...

Code
====

{source}
"""

        response = self.llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        text = response.content

        return AnalysisResult(
            title=f"Code Review - {path.name}",
            score=None,
            summary=text,
        )