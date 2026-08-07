from pprint import pprint

from services.graph.module_resolver import (
    ModuleResolver,
)

resolver = ModuleResolver(
    "repositories/langgraph"
)

lookup = resolver.build_lookup()

print("=" * 60)
print("Module Resolver")
print("=" * 60)

print()

examples = [
    "langgraph.graph.state",
    "langgraph_sdk.client",
    "typing",
    "json",
]

for module in examples:

    print(module)

    pprint(
        lookup.get(module)
    )

    print()