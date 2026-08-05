# 🚀 DevMind AI

> An AI Software Engineering Assistant built with LangChain, LangGraph, and Groq.

DevMind AI understands software repositories, explains code, generates documentation, reviews pull requests, writes unit tests, and helps developers build software faster.

---

## Features

- 📂 Repository Intelligence
- 🔍 Semantic Code Search (RAG)
- 🧠 AI Code Explanation
- 📝 Documentation Generator
- 🧪 Unit Test Generator
- 🐞 Bug Detection
- 🔎 Code Review Assistant
- ⚡ Groq LLM Integration
- 🔗 LangChain + LangGraph
- 🌐 Streamlit Interface (Coming Soon)

---

## Tech Stack

- Python
- LangChain
- LangGraph
- GroqCloud
- FAISS
- HuggingFace Embeddings
- FastAPI
- Streamlit

---

## Installation

```bash
git clone https://github.com/akinwumifakokunde-source/devmind-ai.git

cd devmind-ai

python -m venv .venv

source .venv/bin/activate
# Windows
# .venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file from `.env.example`.

```
GROQ_API_KEY=your_key_here
MODEL_NAME=llama-3.3-70b-versatile
TEMPERATURE=0.2
```

Run

```bash
python main.py
```

---

## Roadmap

- [x] Project Foundation
- [x] Repository Scanner
- [ ] Repository RAG
- [ ] LangGraph Agent
- [ ] Code Review Engine
- [ ] Documentation Generator
- [ ] Streamlit UI
- [ ] GitHub Integration
- [ ] Docker Deployment

---

## License

MIT
