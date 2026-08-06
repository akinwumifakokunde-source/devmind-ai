from agent.tools import list_files

from services.parser import parse_repository
from services.vectorstore import build_vectorstore

print("=" * 60)
print("Building Vector Store")
print("=" * 60)

files = list_files.invoke({}).splitlines()

documents = parse_repository(files)

vectorstore = build_vectorstore(documents)

print()

print(f"Documents indexed: {len(documents)}")

print()

results = vectorstore.similarity_search(
    "repository scanner",
    k=3,
)

print("=" * 60)
print("Top Results")
print("=" * 60)

for doc in results:
    print(doc.metadata["source"])