from langchain_core.messages import HumanMessage

from agent.nodes import assistant

state = {
    "messages": [
        HumanMessage(
            content="List all Python files."
        )
    ]
}

result = assistant(state)

print(result)