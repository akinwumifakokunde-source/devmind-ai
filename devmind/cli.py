import argparse

from services.audit.repository_audit import RepositoryAudit
from services.review.code_reviewer import CodeReviewer
from services.symbol_explainer import SymbolExplainer
from services.graph.repository_graph_builder import RepositoryGraphBuilder
from services.architecture.health_analyzer import RepositoryHealthAnalyzer
from services.graph.graph_queries import GraphQueries
from services.graph.repository_graph_builder import RepositoryGraphBuilder
from services.audit.repository_audit import RepositoryAudit
from services.review.code_reviewer import CodeReviewer
from services.symbol_explainer import SymbolExplainer
from services.graph.repository_graph_builder import RepositoryGraphBuilder
from services.architecture.health_analyzer import RepositoryHealthAnalyzer
from services.graph.impact_analyzer import ImpactAnalyzer


def build_parser():
    parser = argparse.ArgumentParser(
        prog="devmind",
        description=(
            "DevMind AI - AI-powered software engineering "
            "and repository intelligence."
        ),
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="COMMAND",
    )

    audit_parser = subparsers.add_parser(
        "audit",
        help="Run a complete repository audit.",
    )
    audit_parser.add_argument(
        "repository",
        nargs="?",
        default=".",
        help="Repository path. Defaults to the current directory.",
    )

    review_parser = subparsers.add_parser(
        "review",
        help="Review a source file using AI.",
    )
    review_parser.add_argument(
        "file",
        help="Path to the source file.",
    )

    explain_parser = subparsers.add_parser(
        "explain",
        help="Explain a class, function, method, or symbol.",
    )
    explain_parser.add_argument(
        "target",
        help="Symbol to explain.",
    )
    explain_parser.add_argument(
        "--repository",
        "-r",
        default=".",
        help="Repository path. Defaults to the current directory.",
    )

    health_parser = subparsers.add_parser(
        "health",
        help="Analyze repository engineering health.",
    )
    health_parser.add_argument(
        "repository",
        nargs="?",
        default=".",
        help="Repository path. Defaults to the current directory.",
    )

    graph_parser = subparsers.add_parser(
        "graph",
        help="Analyze the repository dependency graph.",
    )
    graph_parser.add_argument(
        "repository",
        nargs="?",
        default=".",
        help="Repository path. Defaults to the current directory.",
    )

    impact_parser = subparsers.add_parser(
        "impact",
        help="Analyze the impact of changing a source file.",
    )
    impact_parser.add_argument(
        "file",
        help="Path to the source file.",
    )

    return parser


def run_audit(repository):
    print()
    print("=" * 60)
    print("DevMind Repository Audit")
    print("=" * 60)
    print()
    print(f"Repository: {repository}")
    print()
    print("Running repository analysis...")
    print()

    audit = RepositoryAudit(repository)
    result = audit.run()

    print("=" * 60)
    print("Repository Health")
    print("=" * 60)
    print()

    health = result.get("health")

    if health:
        for key, value in health.items():
            label = key.replace("_", " ").title()
            print(f"{label}: {value}")

    review = result.get("review")

    if review:
        print()
        print("=" * 60)
        print("AI Code Review")
        print("=" * 60)
        print()

        if hasattr(review, "to_markdown"):
            print(review.to_markdown())
        else:
            print(review)

    print()
    print("=" * 60)
    print("Audit Complete")
    print("=" * 60)
    print()


def run_review(file_path):
    print()
    print("=" * 60)
    print("DevMind AI Code Review")
    print("=" * 60)
    print()

    print(f"File: {file_path}")
    print()
    print("Analyzing code...")
    print()

    reviewer = CodeReviewer()
    result = reviewer.review(file_path)

    if hasattr(result, "to_markdown"):
        print(result.to_markdown())
    else:
        print(result)

    print()
    print("=" * 60)
    print("Review Complete")
    print("=" * 60)
    print()


def run_explain(target, repository):
    print()
    print("=" * 60)
    print("DevMind Symbol Explanation")
    print("=" * 60)
    print()

    print(f"Repository: {repository}")
    print(f"Symbol: {target}")
    print()
    print("Searching repository...")
    print()

    explainer = SymbolExplainer(repository)
    result = explainer.explain(target)

    print("=" * 60)
    print("Explanation")
    print("=" * 60)
    print()
    print(result)

    print()
    print("=" * 60)
    print("Explanation Complete")
    print("=" * 60)
    print()


def run_health(repository):
    print()
    print("=" * 60)
    print("DevMind Repository Health")
    print("=" * 60)
    print()

    print(f"Repository: {repository}")
    print()
    print("Building repository graph...")
    print()

    builder = RepositoryGraphBuilder(repository)
    graph = builder.build()

    print("Analyzing repository health...")
    print()

    analyzer = RepositoryHealthAnalyzer(graph)
    result = analyzer.analyze()

    print("=" * 60)
    print("Health Analysis")
    print("=" * 60)
    print()

    for key, value in result.items():
        label = key.replace("_", " ").title()
        print(f"{label}: {value}")

    print()
    print("=" * 60)
    print("Health Analysis Complete")
    print("=" * 60)
    print()
def run_graph(repository):
    print()
    print("=" * 60)
    print("DevMind Repository Graph")
    print("=" * 60)
    print()

    print(f"Repository: {repository}")
    print()
    print("Building repository graph...")
    print()

    builder = RepositoryGraphBuilder(repository)
    graph = builder.build()

    queries = GraphQueries(graph)
    stats = queries.statistics()

    print("=" * 60)
    print("Graph Statistics")
    print("=" * 60)
    print()

    print(f"Modules: {stats.get('modules', 0)}")
    print(f"Imports: {stats.get('imports', 0)}")

    print()

    ranked = []

    for node in graph.modules.values():
        ranked.append(
            (
                len(node.imports),
                node.name,
            )
        )

    ranked.sort(reverse=True)

    print("=" * 60)
    print("Most Connected Modules")
    print("=" * 60)
    print()

    for imports, module in ranked[:10]:
        print(f"{module}: {imports} imports")

    print()
    print("=" * 60)
    print("Graph Analysis Complete")
    print("=" * 60)
    print()

def run_impact(file_path):
    print()
    print("=" * 60)
    print("DevMind Impact Analysis")
    print("=" * 60)
    print()

    print(f"File: {file_path}")
    print()
    print("Building repository graph...")
    print()

    # The graph must be built from the repository root.
    repository = "."

    builder = RepositoryGraphBuilder(repository)
    graph = builder.build()

    analyzer = ImpactAnalyzer(graph)

    # Convert Windows path to the repository graph's
    # normalized POSIX-style module path.
    module = file_path.replace("\\", "/")

    result = analyzer.analyze(module)

    print("=" * 60)
    print("Impact Analysis")
    print("=" * 60)
    print()

    print(f"Module: {result['module']}")
    print(f"Risk: {result['risk']}")
    print(f"Total Affected Modules: {result['total']}")

    print()

    print("Direct Dependents")
    print("-" * 20)

    if result["direct"]:
        for item in result["direct"]:
            print(f"- {item}")
    else:
        print("- None")

    print()

    print("Indirect Dependents")
    print("-" * 20)

    if result["indirect"]:
        for item in result["indirect"]:
            print(f"- {item}")
    else:
        print("- None")

    print()
    print("=" * 60)
    print("Impact Analysis Complete")
    print("=" * 60)
    print()

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "audit":
        run_audit(args.repository)
        return

    if args.command == "review":
        run_review(args.file)
        return

    if args.command == "explain":
        run_explain(args.target, args.repository)
        return

    if args.command == "health":
        run_health(args.repository)
        return

    if args.command == "graph":
        run_graph(args.repository)
        return

    if args.command == "impact":
        run_impact(args.file)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
