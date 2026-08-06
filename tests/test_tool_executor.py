from langchain_core.messages import HumanMessage

from agent.nodes import assistant
from agent.tool_executor import execute_tool

state = {
    "messages": [
        HumanMessage(
            content="List all Python files."
        )
    ]
}

response = assistant(state)

ai_message = response["messages"][0]

print("=" * 60)
print("LLM Decision")
print("=" * 60)

print(ai_message.additional_kwargs["tool_call"])

print("=" * 60)
print("Tool Result")
print("=" * 60)

result = execute_tool(ai_message)

print(result)