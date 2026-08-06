from pathlib import Path

from langchain_community.vectorstores import FAISS

from services.embeddings import get_embeddings

INDEX_DIR = Path("faiss_index")


def build_vectorstore(documents):
    """
    Build or load a FAISS vector store.
    """

    embeddings = get_embeddings()

    if (
        INDEX_DIR.exists()
        and (INDEX_DIR / "index.faiss").exists()
        and (INDEX_DIR / "index.pkl").exists()
    ):

        print("Loading existing FAISS index...")

        return FAISS.load_local(
            str(INDEX_DIR),
            embeddings,
            allow_dangerous_deserialization=True,
        )

    print("Building new FAISS index...")

    vectorstore = FAISS.from_documents(
        documents,
        embeddings,
    )

    INDEX_DIR.mkdir(exist_ok=True)

    vectorstore.save_local(str(INDEX_DIR))

    print("FAISS index saved.")

    return vectorstore