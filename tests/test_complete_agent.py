from langchain_core.messages import HumanMessage

from agent.nodes import assistant
from agent.tool_executor import execute_tool
from agent.final_answer import generate_final_answer

question = "List all Python files."

state = {
    "messages": [
        HumanMessage(content=question)
    ]
}

response = assistant(state)

ai_message = response["messages"][0]

tool_result = execute_tool(ai_message)

answer = generate_final_answer(
    question,
    tool_result,
)

print("=" * 60)
print(answer)
print("=" * 60)