import os

from dotenv import load_dotenv

from langchain_core.messages import AIMessage
from langchain_groq import ChatGroq

from services.retriever import RepositoryRetriever

load_dotenv()

retriever = RepositoryRetriever()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("MODEL_NAME"),
    temperature=0.2,
)


def retrieve(state):

    question = state["messages"][-1].content

    context = retriever.search(question)

    return {
        "context": context
    }


def assistant(state):

    question = state["messages"][-1].content

    context = state["context"]

    prompt = f"""
You are DevMind AI.

You are an expert software engineer.

Use ONLY the repository context.

Repository:

{context}

Question:

{question}
"""

    response = llm.invoke(prompt)

    return {
        "messages": [
            AIMessage(content=response.content)
        ]
    }