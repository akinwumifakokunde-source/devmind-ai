from agent.tools import list_files
from services.parser import parse_repository

files = list_files.invoke({}).splitlines()

documents = parse_repository(files)

print("=" * 60)
print(f"Loaded {len(documents)} documents")
print("=" * 60)

doc = documents[0]

print(doc.metadata)
print("-" * 60)
print(doc.page_content[:500])