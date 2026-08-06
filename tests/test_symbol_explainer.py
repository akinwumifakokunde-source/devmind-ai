from agent.tools import explain_symbol

result = explain_symbol.invoke(
    {
        "name": "StateGraph"
    }
)

print(result)