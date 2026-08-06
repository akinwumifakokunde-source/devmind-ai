import json

from langchain_core.messages import AIMessage

from agent.tools import tools
from services.llm import get_llm

llm = get_llm()


def build_tool_prompt() -> str:
    """
    Build the available tool list dynamically.
    """

    sections = []

    for tool in tools:

        sections.append(
            f"""
Tool:
{tool.name}

Description:
{tool.description}
"""
        )

    return "\n".join(sections)


TOOL_PROMPT = build_tool_prompt()


def assistant(state):
    """
    Decide which tool to execute.
    """

    user_question = state["messages"][-1].content

    prompt = f"""
You are DevMind AI.

You are an expert software engineering assistant.

You have the following tools available.

========================================

{TOOL_PROMPT}

========================================

Choose ONE tool.

Tool Selection Rules

1.
Questions like

Explain parser.py

Explain services/parser.py

→ explain_file

----------------------------

2.
Questions like

Explain StateGraph

Explain RunnableCallable

Explain Command

Explain Pregel

Explain StateGraph.compile()

→ explain_symbol

----------------------------

3.
Questions like

Find symbol StateGraph

Where is StateGraph defined?

Where is RunnableCallable?

Where is Command defined?

→ find_symbol

----------------------------

4.
Questions like

Read parser.py

Open services/parser.py

→ read_file

----------------------------

5.
Questions like

List files

Show project files

→ list_files

----------------------------

6.
Everything else related to repository knowledge

→ search_repository

========================================

Return ONLY valid JSON.

Examples

{{
    "tool": "find_symbol",
    "arguments": {{
        "name": "StateGraph"
    }}
}}

{{
    "tool": "explain_symbol",
    "arguments": {{
        "name": "RunnableCallable"
    }}
}}

{{
    "tool": "read_file",
    "arguments": {{
        "path": "services/parser.py"
    }}
}}

User Question

{user_question}
"""

    response = llm.invoke(prompt)

    try:
        tool_call = json.loads(response.content)

    except Exception:

        tool_call = {
            "tool": "search_repository",
            "arguments": {
                "query": user_question
            },
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