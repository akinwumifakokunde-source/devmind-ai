from langchain_core.messages import HumanMessage

from agent.workflow import workflow

result = workflow.invoke(
    {
        "messages": [
            HumanMessage(
                content="Explain RepositoryRetriever"
            )
        ]
    }
)

print(result["messages"][-1].content)