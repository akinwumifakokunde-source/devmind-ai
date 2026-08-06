from pathlib import Path

from services.architecture.component_detector import ComponentDetector
from services.architecture.entrypoint_detector import EntrypointDetector
from services.architecture.framework_detector import FrameworkDetector
from services.repository_scanner import RepositoryScanner
from services.symbol_index import SymbolIndexer


class ArchitectureAnalyzer:
    """
    Performs deterministic repository analysis.

    This class does NOT use an LLM.
    It gathers structured information about the repository
    that can later be passed to an LLM for reasoning.
    """

    def __init__(self, repository):

        self.repository = Path(repository).resolve()

        self.scanner = RepositoryScanner(self.repository)

        self.component_detector = ComponentDetector(
            self.repository
        )

        self.framework_detector = FrameworkDetector(
            self.repository
        )

        self.entrypoint_detector = EntrypointDetector(
            self.repository
        )

        self.symbol_index = SymbolIndexer()

    def analyze(self):

        # ---------------------------------------------------------
        # Repository statistics
        # ---------------------------------------------------------

        stats = self.scanner.summary()

        # ---------------------------------------------------------
        # Components
        # ---------------------------------------------------------

        components = self.component_detector.detect()

        # ---------------------------------------------------------
        # Frameworks
        # ---------------------------------------------------------

        frameworks = self.framework_detector.detect()

        # ---------------------------------------------------------
        # Entrypoints
        # ---------------------------------------------------------

        entrypoints = self.entrypoint_detector.detect()

        # ---------------------------------------------------------
        # Symbols
        # ---------------------------------------------------------

        self.symbol_index.build(self.repository)

        symbol_count = len(self.symbol_index.index)

        # ---------------------------------------------------------
        # Final summary
        # ---------------------------------------------------------

        return {
            "project": self.repository.name,
            "repository": str(self.repository),
            "language": "Python",
            "files": stats["files"],
            "python_files": stats["python_files"],
            "frameworks": frameworks,
            "components": components,
            "entrypoints": entrypoints,
            "symbols": symbol_count,
        }