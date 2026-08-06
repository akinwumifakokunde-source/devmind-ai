from services.embeddings import get_embeddings

embeddings = get_embeddings()

vector = embeddings.embed_query(
    "Explain how LangGraph works."
)

print("=" * 60)
print(f"Embedding length: {len(vector)}")
print("=" * 60)

print(vector[:10])