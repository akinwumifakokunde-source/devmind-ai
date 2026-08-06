from agent.tools import explain_file

print("=" * 60)
print("Testing explain_file")
print("=" * 60)

result = explain_file.invoke(
    {
        "path": "services/parser.py"
    }
)

print(result)