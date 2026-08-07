from pprint import pprint

from services.audit.repository_audit import RepositoryAudit

audit = RepositoryAudit(".")

result = audit.run()

print("=" * 60)
print("Repository Audit")
print("=" * 60)

print()

print("Health")
print("-" * 20)
pprint(result["health"])

print()

print("AI Code Review")
print("-" * 20)
print(result["review"].to_markdown())