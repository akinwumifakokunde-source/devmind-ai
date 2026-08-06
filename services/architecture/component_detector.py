from pathlib import Path


COMPONENT_RULES = {
    "api": {
        "api",
        "routes",
        "route",
        "controllers",
        "controller",
        "endpoints",
    },
    "services": {
        "services",
        "service",
    },
    "models": {
        "models",
        "model",
        "entities",
    },
    "repositories": {
        "repositories",
        "repository",
        "dao",
    },
    "database": {
        "database",
        "db",
        "migrations",
    },
    "config": {
        "config",
        "configs",
        "settings",
    },
    "tests": {
        "tests",
        "test",
    },
    "docs": {
        "docs",
        "documentation",
    },
    "frontend": {
        "frontend",
        "client",
        "web",
        "ui",
        "react",
        "next",
    },
    "scripts": {
        "scripts",
        "script",
    },
    "utils": {
        "utils",
        "helpers",
        "common",
    },
}


class ComponentDetector:

    def __init__(self, repository):

        self.repository = Path(repository)

    def detect(self):

        components = {
            key: []
            for key in COMPONENT_RULES
        }

        discovered = set()

        for path in self.repository.rglob("*"):

            if not path.is_dir():
                continue

            name = path.name.lower()

            for component, aliases in COMPONENT_RULES.items():

                if name in aliases:

                    relative = (
                        path.relative_to(self.repository)
                        .as_posix()
                    )

                    if relative not in discovered:

                        discovered.add(relative)

                        components[component].append(relative)

        return {
            key: sorted(value)
            for key, value in components.items()
            if value
        }