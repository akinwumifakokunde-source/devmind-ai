from dataclasses import dataclass, field


@dataclass
class ModuleNode:
    """
    Represents one Python module.
    """

    name: str

    imports: set[str] = field(default_factory=set)

    internal: set[str] = field(default_factory=set)

    external: set[str] = field(default_factory=set)


@dataclass
class RepositoryGraph:
    """
    Complete dependency graph.
    """

    modules: dict[str, ModuleNode] = field(
        default_factory=dict
    )

    def add_module(self, name: str):

        if name not in self.modules:

            self.modules[name] = ModuleNode(
                name=name
            )

        return self.modules[name]

    def module(self, name: str):

        return self.modules.get(name)

    def __contains__(self, name):

        return name in self.modules

    def __len__(self):

        return len(self.modules)