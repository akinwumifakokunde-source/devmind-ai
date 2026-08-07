# 🚀 DevMind AI

> AI-powered software engineering platform for understanding, auditing, reviewing, and documenting code repositories.

DevMind AI helps developers and engineering teams understand unfamiliar codebases using repository intelligence, graph analysis, retrieval-augmented generation (RAG), and large language models.

---

## ✨ Features

### 🤖 AI Repository Assistant

- Chat with any GitHub repository
- Semantic repository search (RAG)
- Explain classes, functions, and methods
- Find symbols instantly
- Explain entire source files

---

### 🏗 Repository Intelligence

- Repository Graph Builder
- Module Resolver
- Symbol Indexing
- Symbol Explanation
- Framework Detection
- Entry Point Detection
- Component Detection

---

### 🔗 Dependency Analysis

- Dependency Graph
- Reverse Dependency Graph
- Circular Dependency Detection
- Repository Graph Queries
- Impact Analysis
- Dependency Statistics

---

### 🏛 Architecture Analysis

- Repository Health Analysis
- Architecture Diagrams
- Mermaid Diagram Generation
- Engineering Architecture Reports
- Repository Statistics

---

### 🧠 AI Engineering

- AI Code Review
- Repository Audit
- Engineering Recommendations
- Code Quality Analysis
- Maintainability Assessment
- Architecture Intelligence

---

## Repository Audit

Run a complete engineering audit on any repository.

```
Repository

↓

Repository Graph

↓

Dependency Analysis

↓

Architecture Analysis

↓

Repository Health

↓

Impact Analysis

↓

AI Code Review

↓

Engineering Report
```

---

## Current Architecture

```
Git Repository
      │
      ▼
Repository Intelligence
      │
 ┌────┴─────────────┐
 │                  │
 ▼                  ▼
Semantic Search   Graph Analysis
 │                  │
 ▼                  ▼
Symbol Index   Dependency Analysis
 │                  │
 └──────────┬───────┘
            ▼
Repository Audit
            ▼
AI Code Review
            ▼
Engineering Report
```

---

## Technology Stack

- Python
- LangChain
- LangGraph
- Groq
- FAISS
- Hugging Face
- GitPython
- Tree-sitter
- NetworkX
- Pydantic

---

## Project Structure

```
services/
│
├── architecture/
├── audit/
├── graph/
├── review/
├── models/
├── parser/
├── retriever/
├── vectorstore/
├── symbol_index/
└── chat_session/

tests/

repositories/

docs/
```

---

## Example Usage

### Repository Chat

```bash
python -m tests.test_chat
```

### Repository Audit

```bash
python -m tests.test_repository_audit
```

### AI Code Review

```bash
python -m tests.test_code_reviewer
```

### Repository Health

```bash
python -m tests.test_repository_health
```

### Impact Analysis

```bash
python -m tests.test_impact_analyzer
```

---

## Roadmap

### ✅ v0.3.0

- AI Repository Chat
- Repository Intelligence
- Symbol Index
- Repository Graph
- Dependency Analysis
- Reverse Dependency Graph
- Circular Dependency Detection
- Repository Health
- Impact Analysis
- Architecture Diagram
- Mermaid Generator
- AI Code Review
- Repository Audit
- Engineering Report Foundation

### 🚧 v0.4.0

- DevMind CLI
- Engineering Report Export
- Markdown Export
- JSON Export
- HTML Export
- PDF Export

### 🔜 v0.5.0

- GitHub Action
- VS Code Extension
- REST API
- MCP Server
- Multi-language Support

---

## Vision

DevMind AI aims to become an intelligent software engineering companion that helps developers:

- Understand unfamiliar codebases
- Detect architectural issues
- Review code intelligently
- Measure engineering health
- Generate engineering documentation
- Improve software quality with AI

---

## Contributing

Contributions are welcome.

Feel free to submit issues, feature requests, or pull requests.

---

## License

![Python](https://img.shields.io/badge/Python-3.13-blue)

![LangChain](https://img.shields.io/badge/LangChain-1.3-green)

![LangGraph](https://img.shields.io/badge/LangGraph-Latest-orange)

![License](https://img.shields.io/badge/license-MIT-red)


