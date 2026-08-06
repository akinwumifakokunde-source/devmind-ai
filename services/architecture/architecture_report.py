import json

from langchain_core.messages import HumanMessage

from services.llm import get_llm

llm = get_llm()


class ArchitectureReportGenerator:

    def generate(self, summary: dict):

        prompt = f"""
You are DevMind AI.

You are an expert Software Architect.

You are given a structured analysis of a software repository.

Repository Summary
==================

{json.dumps(summary, indent=2)}

Generate a professional architecture report.

Return EXACTLY this format.

# Repository Overview

A short summary of the repository.

# Architecture

Describe the architecture pattern.

# Main Components

Explain every detected component.

# Technology Stack

Explain the purpose of each framework.

# Entry Points

Explain how the application starts.

# Repository Statistics

Summarize the repository size.

# Strengths

Highlight engineering strengths.

# Improvement Opportunities

Suggest architectural improvements.

Rules

- Use only the provided repository summary.
- Do NOT invent frameworks or files.
- Keep the report concise.
- Write like a Principal Software Architect.
"""

        response = llm.invoke(
            [
                HumanMessage(
                    content=prompt
                )
            ]
        )

        return response.content