from langchain_core.messages import HumanMessage

from services.llm import get_llm

llm = get_llm()


def generate_final_answer(question: str, tool_result: dict) -> str:
    """
    Generate a repository-aware answer.
    """

    context = tool_result["context"]
    sources = tool_result["sources"]

    prompt = f"""
You are DevMind AI.

Answer ONLY using the repository context.

If the answer is not available in the repository, say so.

Repository Context
==================

{context}

Question
========

{question}

Return your answer using:

# Summary

# Explanation
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    answer = response.content.strip()

    if sources:

        answer += "\n\n# Sources\n"

        for source in sources:
            answer += f"\n- {source}"

    return answer