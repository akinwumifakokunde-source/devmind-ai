from langchain_core.messages import HumanMessage

from services.code_reader import read_around_line
from services.llm import get_llm
from services.symbol_index import SymbolIndexer


llm = get_llm()


class SymbolExplainer:

    def __init__(self, repository):

        self.repository = repository

        self.index = SymbolIndexer()

        self.index.build(repository)

    def explain(self, symbol: str):

        matches = self.index.find(symbol)

        if not matches:
            return f"Symbol '{symbol}' not found."

        match = matches[0]

        code = read_around_line(
            self.repository,
            match["file"],
            match["line"],
        )

        prompt = f"""
You are DevMind AI.

Explain this code.

Symbol:
{symbol}

File:
{match["file"]}

Code
====

{code}

Return:

# Purpose

# Parameters

# Workflow

# Return Value

# Related Components

# Improvements
"""

        response = llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content