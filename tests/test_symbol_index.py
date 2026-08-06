from services.symbol_index import SymbolIndexer

indexer = SymbolIndexer()

indexer.build(
    "repositories/langgraph"
)

print(indexer.find("StateGraph"))

print(indexer.find("compile"))

print(indexer.find("Command"))