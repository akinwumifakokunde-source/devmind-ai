from agent.tools import (
    list_files,
    read_file,
    search_repository,
)

print("=" * 60)
print("LIST FILES")
print("=" * 60)

print(list_files.invoke({}))

print()

print("=" * 60)
print("READ FILE")
print("=" * 60)

print(read_file.invoke({"path": "README.md"}))

print()

print("=" * 60)
print("SEARCH")
print("=" * 60)

print(search_repository.invoke(
    {"query": "RepositoryRetriever"}
))