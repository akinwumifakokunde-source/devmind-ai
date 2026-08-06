from services.retriever import RepositoryRetriever

retriever = RepositoryRetriever()

queries = [
    "repository scanner",
    "vector store",
    "embeddings",
    "main entry point",
    "agent",
]

for query in queries:

    print("=" * 70)
    print("QUERY:", query)
    print("=" * 70)

    docs = retriever.search(query)

    for doc in docs:
        print(doc.metadata["source"])

    print()