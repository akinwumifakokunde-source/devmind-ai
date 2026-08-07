from services.review.code_reviewer import CodeReviewer


reviewer = CodeReviewer()

result = reviewer.review(
    "services/retriever.py"
)

print()
print("=" * 60)
print("AI Code Review")
print("=" * 60)
print()

print(
    result.to_markdown()
)