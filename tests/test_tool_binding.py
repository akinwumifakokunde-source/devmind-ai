from agent.agent import DevMindAgent

agent = DevMindAgent()

response = agent.llm.invoke(
    "List every Python file in this repository."
)

print(response)