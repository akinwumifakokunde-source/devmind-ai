from pathlib import Path


class ModuleResolver:
    """
    Resolves Python import names to repository files.

    Example:

    libs/sdk-py/langgraph_sdk/client.py

    becomes

    langgraph_sdk.client
    client

    """

    def __init__(self, repository):

        self.repository = Path(repository)

    def build_lookup(self):

        lookup = {}

        for file in self.repository.rglob("*.py"):

            relative = file.relative_to(
                self.repository
            ).as_posix()

            module = relative[:-3]

            parts = module.split("/")

            # remove __init__
            if parts[-1] == "__init__":
                parts.pop()

            # Generate every possible dotted name
            #
            # libs/langgraph/langgraph/graph/state.py
            #
            # ->
            # libs.langgraph.langgraph.graph.state
            # langgraph.langgraph.graph.state
            # langgraph.graph.state
            # graph.state
            # state

            for i in range(len(parts)):

                dotted = ".".join(parts[i:])

                lookup[dotted] = relative

        return lookup