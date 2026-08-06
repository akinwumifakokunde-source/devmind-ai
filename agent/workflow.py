from langgraph.graph import StateGraph
from langgraph.graph import START, END

from agent.state import AgentState
from agent.nodes import retrieve, assistant

builder = StateGraph(AgentState)

builder.add_node("retrieve", retrieve)
builder.add_node("assistant", assistant)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "assistant")
builder.add_edge("assistant", END)

workflow = builder.compile()