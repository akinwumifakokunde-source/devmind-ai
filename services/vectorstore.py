from langchain_community.vectorstores import FAISS

from services.embeddings import get_embeddings


def build_vectorstore(documents):
    """
    Build a FAISS vector database from LangChain Documents.
    """

    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        documents,
        embeddings,
    )

    return vectorstore