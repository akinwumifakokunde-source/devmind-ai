from pathlib import Path

from langchain_community.vectorstores import FAISS

from services.embeddings import get_embeddings


def build_vectorstore(documents, index_dir: Path):
    """
    Build or load a FAISS vector store for a specific repository.
    """

    embeddings = get_embeddings()

    index_dir = Path(index_dir)

    if (
        index_dir.exists()
        and (index_dir / "index.faiss").exists()
        and (index_dir / "index.pkl").exists()
    ):

        print(f"Loading existing FAISS index: {index_dir}")

        return FAISS.load_local(
            str(index_dir),
            embeddings,
            allow_dangerous_deserialization=True,
        )

    print(f"Building new FAISS index: {index_dir}")

    vectorstore = FAISS.from_documents(
        documents,
        embeddings,
    )

    index_dir.mkdir(parents=True, exist_ok=True)

    vectorstore.save_local(str(index_dir))

    print("FAISS index saved.")

    return vectorstore