from services.project_analyzer import ProjectAnalyzer

analyzer = ProjectAnalyzer()

retriever = analyzer.analyze(
    "https://github.com/langchain-ai/langgraph"
)

print("=" * 60)
print("QUESTION")
print("=" * 60)

result = retriever.search(
    "What is StateGraph?"
)

print(result[:3000])