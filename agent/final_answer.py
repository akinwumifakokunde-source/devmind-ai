from langchain_core.messages import HumanMessage

from services.llm import get_llm

llm = get_llm()


def generate_final_answer(question: str, tool_result: str):

    prompt = f"""
You are DevMind AI.

A tool has already been executed.

User Question
-------------

{question}

Tool Output
-----------

{tool_result}

Write a concise, professional answer.

Do not mention tools.

Summarize the result clearly.
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return response.content