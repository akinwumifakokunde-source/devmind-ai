# DevMind AI

> Open-source AI Software Engineering Intelligence Platform for understanding, documenting, and analyzing code repositories.

DevMind is an AI-powered developer platform that combines **repository-aware Retrieval-Augmented Generation (RAG)**, **static code analysis**, **symbol indexing**, and **software architecture intelligence** to help developers understand complex codebases.

Instead of treating a repository as plain text, DevMind builds a structured understanding of the project before using LLMs to answer questions.

---

## ✨ Features

### Repository Intelligence

- 🔍 Semantic repository search
- 📚 Repository-specific FAISS indexes
- 📁 Repository scanning
- 🧠 AI repository chat
- 📄 Read and explain source files

### Symbol Intelligence

- 🔎 Symbol indexing
- 📍 Find classes and functions
- 🧩 Explain classes, methods and functions
- 📖 Source-aware code explanations

### Architecture Intelligence

- 🏗 Component detection
- ⚙️ Framework detection
- 🚀 Entry point detection
- 📊 Repository architecture analysis
- 🤖 AI-generated architecture reports

---

## Example Questions

```
Explain StateGraph

Where is RunnableCallable defined?

Explain services/parser.py

List project files

Explain the repository architecture

How does this project work?

What frameworks does this repository use?
```

---

## Current Architecture

```text
Git Repository
       │
       ▼
Repository Scanner
       │
       ▼
Semantic Repository Index (FAISS)
       │
       ▼
Symbol Index
       │
       ▼
Architecture Analyzer
       │
       ▼
Large Language Model
       │
       ▼
Developer Insights
```

---

## Project Structure

```
DevMind
│
├── agent/
│
├── services/
│   ├── architecture/
│   │   ├── architecture_analyzer.py
│   │   ├── architecture_report.py
│   │   ├── component_detector.py
│   │   ├── entrypoint_detector.py
│   │   └── framework_detector.py
│   │
│   ├── retriever.py
│   ├── symbol_index.py
│   ├── symbol_explainer.py
│   ├── vectorstore.py
│   └── ...
│
├── tests/
│
└── repositories/
```

---

## Current Capabilities

- Repository-aware AI chat
- Semantic code search
- Symbol lookup
- Symbol explanation
- File explanation
- Repository architecture analysis
- Technology stack detection
- Component discovery
- Entry point discovery

---

# Roadmap

## ✅ v0.2.0 — Repository Intelligence

- Repository Chat
- Semantic Repository Search
- Repository-specific FAISS Indexes
- Symbol Indexing
- Explain Classes & Functions
- Explain Source Files
- Component Detection
- Framework Detection
- Entry Point Detection
- Architecture Analyzer
- AI Architecture Reports

---

## 🚧 v0.3.0 — Dependency Intelligence

- AST Dependency Graph
- Mermaid Diagram Generator
- Module Relationship Graph
- Repository Visualization
- Architecture Explorer

---

## 🔜 v0.4.0 — Engineering Intelligence

- AI Code Review
- Security Analysis
- Technical Debt Detection
- Refactoring Suggestions
- Dead Code Detection

---

## 🔜 v0.5.0 — Developer Experience

- VS Code Extension
- GitHub Action
- Command Line Interface (CLI)
- Model Context Protocol (MCP) Server
- REST API

---

## Technology Stack

- Python
- LangChain
- LangGraph
- FAISS
- Hugging Face Embeddings
- Groq LLMs
- GitPython
- AST
- FastAPI (planned)

---

## Vision

DevMind aims to become an **AI Software Engineering Intelligence Platform** that helps developers:

- Understand unfamiliar repositories
- Explore software architecture
- Navigate large codebases
- Generate technical documentation
- Review code intelligently
- Improve software quality

---

## Contributing

Contributions, feature requests, and pull requests are welcome.

If you'd like to help improve DevMind, feel free to open an issue or submit a pull request.


---

## ⭐ Support the Project

If you find DevMind useful, consider giving the repository a ⭐ on GitHub to support its development.
---

## License
![Python](https://img.shields.io/badge/Python-3.13-blue)

![LangChain](https://img.shields.io/badge/LangChain-1.3-green)

![LangGraph](https://img.shields.io/badge/LangGraph-Latest-orange)

![License](https://img.shields.io/badge/license-MIT-red)


