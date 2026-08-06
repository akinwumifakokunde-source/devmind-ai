from agent.tools import tools

TOOL_MAP = {
    tool.name: tool
    for tool in tools
}


def execute_tool(ai_message):

    tool_call = ai_message.additional_kwargs["tool_call"]

    tool_name = tool_call["tool"]

    arguments = tool_call["arguments"]

    if tool_name == "none":
        return None

    tool = TOOL_MAP[tool_name]

    result = tool.invoke(arguments)

    return result