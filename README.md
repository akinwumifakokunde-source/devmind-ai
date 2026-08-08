# 🚀 DevMind AI

> Open-source AI software engineering platform for understanding repositories, analyzing architecture, reviewing code, detecting dependencies, and generating engineering insights.

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1.3-green)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-AI%20Workflows-orange)](https://www.langchain.com/langgraph)
[![License](https://img.shields.io/badge/license-MIT-red)](LICENSE)

DevMind AI helps developers and engineering teams understand unfamiliar codebases by combining **repository intelligence, dependency graphs, architecture analysis, change-impact analysis, symbol intelligence, RAG, and AI-powered code review**.

## ✨ What DevMind Does

### 🤖 AI Repository Intelligence

- AI-powered repository understanding
- Semantic repository search (RAG)
- Explain classes, functions, methods, and symbols
- Explain complete source files
- Symbol indexing and resolution
- Repository-aware AI context

### 🔗 Dependency Intelligence

- Repository dependency graph
- Direct and reverse dependencies
- Dependency statistics
- Circular dependency detection
- Graph queries
- Module resolution
- Change-impact analysis
- Direct and indirect dependency analysis

### 🏗️ Architecture Intelligence

- Repository health analysis
- Architecture scoring
- Architecture diagrams
- Mermaid diagram generation
- Repository statistics
- Framework detection
- Entry-point detection
- Component detection
- Engineering architecture reports

### 🧠 AI Engineering

- AI code review
- Repository audit
- Code quality analysis
- Maintainability assessment
- Engineering recommendations
- Architecture intelligence
- Risk and impact assessment

## ⚡ DevMind CLI

DevMind provides a command-line interface for repository intelligence.


                    DevMind CLI
                         │
        ┌────────────────┼────────────────┐
        │                │                │
      Audit            Review           Explain
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
              Repository Intelligence
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
       Symbol Intelligence      Graph Intelligence
             │                       │
             ▼                 ┌─────┴─────┐
       Semantic Search         │           │
             │              Dependencies  Cycles
             │                 │           │
             └─────────────────┼───────────┘
                               ▼
                       Impact Analysis
                               │
                               ▼
                       Health Analysis
                               │
                               ▼
                       AI Engineering
                               │
                               ▼
                    Engineering Insights


                    devmind-ai/

 Project Structure
 
devmind-ai/
├── devmind/
│   ├── __init__.py
│   ├── __main__.py
│   └── cli.py
│
├── services/
│   ├── architecture/
│   ├── audit/
│   ├── graph/
│   ├── models/
│   ├── review/
│   ├── parser/
│   ├── retriever/
│   ├── symbol_index/
│   └── vectorstore/
│
├── tests/
├── agent/
├── api/
├── ui/
├── requirements.txt
└── README.md

🛠️ Technology Stack
Python
LangChain
LangGraph
Groq
RAG
FAISS
Hugging Face
GitPython
NetworkX
Pydantic
Python AST analysis


Testing

python -m tests.test_graph_queries
python -m tests.test_impact_analyzer
python -m tests.test_repository_health
python -m tests.test_repository_audit
python -m tests.test_code_reviewer
python -m tests.test_repository_graph_builder
python -m tests.test_circular_dependency_detector
python -m tests.test_module_resolver
python -m tests.test_analysis_result


📊 Engineering Intelligence

DevMind is designed to answer questions such as:

What does this module depend on?
What depends on this module?
What will be affected if I change this file?
Are there circular dependencies?
Which modules are most connected?
How healthy is this repository?
What is the architecture of this codebase?
What does this class or function actually do?
Where are the potential engineering risks?
How can this code be improved?
🛣️ Roadmap
✅ v0.4.0 — Core CLI Intelligence
DevMind CLI
Repository audit
Repository health
Dependency graph
Reverse dependency analysis
Circular dependency detection
Change-impact analysis
AI code review
Symbol explanation
Repository graph engine
Architecture analysis
Engineering recommendations
🔜 v0.5.0
GitHub Action
Pull request analysis
Git diff impact analysis
VS Code extension
REST API
MCP server
Multi-language repository support
Machine-readable engineering reports
🎯 Vision

DevMind AI is being built toward an intelligent software engineering platform that understands software at the repository and system level, rather than only analyzing individual files.

Code
  ↓
Symbols
  ↓
Modules
  ↓
Dependencies
  ↓
Architecture
  ↓
Change Impact
  ↓
Engineering Health
  ↓
AI Engineering Insights

Understand repositories. Analyze architecture. Review code. Predict impact.

🤝 Contributing

Contributions are welcome.

Feel free to submit issues, feature requests, or pull requests.


```bash
python -m devmind --help
