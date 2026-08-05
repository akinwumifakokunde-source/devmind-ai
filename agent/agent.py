import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()


class DevMindAgent:

    def __init__(self):

        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("MODEL_NAME"),
            temperature=0.2,
        )

    def chat(self, question: str):

        response = self.llm.invoke(
            [
                HumanMessage(question)
            ]
        )

        return response.content