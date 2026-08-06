import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from services.retriever import RepositoryRetriever

load_dotenv()


class DevMindAgent:

    def __init__(self):

        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("MODEL_NAME"),
            temperature=0.2,
        )

        self.retriever = RepositoryRetriever()

    def chat(self, question: str):

        context = self.retriever.search(question)

        prompt = f"""

You are DevMind AI, an expert software engineering assistant.

Use ONLY the repository context below.

When answering:
- Mention filenames when relevant.
- Explain how components interact.
- Quote code only when necessary.
- If the repository doesn't contain the answer, say:

  "I couldn't find that in this repository."

Repository Context
------------------

{context}

User Question
-------------

{question}
"""

        response = self.llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content