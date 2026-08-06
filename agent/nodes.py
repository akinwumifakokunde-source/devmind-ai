import json

from langchain_core.messages import AIMessage

from services.llm import get_llm

llm = get_llm()


def assistant(state):

    messages = state["messages"]

    user_question = messages[-1].content

    prompt = f"""
You are DevMind AI.

You have access to these tools:

1. list_files
Arguments:
{{"directory": "."}}

2. read_file
Arguments:
{{"path": "services/parser.py"}}

3. search_repository
Arguments:
{{"query": "..."}}

4. explain_file
Arguments:
{{"path": "services/parser.py"}}

Choose the BEST tool.

Return ONLY valid JSON.

Example:

{{
    "tool": "list_files",
    "arguments": {{
        "directory": "."
    }}
}}

User:

{user_question}
"""

    response = llm.invoke(prompt)

    try:
        tool_call = json.loads(response.content)

    except Exception:

        tool_call = {
            "tool": "none",
            "arguments": {}
        }

    return {
        "messages": [
            AIMessage(
                content=response.content,
                additional_kwargs={
                    "tool_call": tool_call
                }
            )
        ]
    }