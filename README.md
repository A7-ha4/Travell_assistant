# 🧭 Traveller Assistance AI

An intelligent travel assistant built with Django, LangChain, and Ollama — powered by local LLMs and a custom RAG pipeline. This project uses vector-based document retrieval to provide context-aware answers for all your travel-related queries.

---

## 🚀 Features

- 🔗 LangChain-based pipeline with custom prompts and document loaders
- 🦙 Local LLM served via Ollama (LLaMA 3 - 8B)
- 🧬 `maxbai-embed-large` used for embedding document chunks
- 📚 Retrieval-Augmented Generation (RAG) with ChromaDB vector store
- 🧠 Maintains chat history using conversation memory
- 🖥️ Django-powered web interface for smooth interaction
- 🔍 Accurate, document-grounded responses from local knowledge base

---

## 🛠️ Tech Stack

| Tool               | Purpose                                  |
|--------------------|------------------------------------------|
| **LangChain**       | RAG pipeline, memory, and prompt chaining |
| **Ollama**          | Local LLM backend (LLaMA 3 8B)           |
| **maxbai-embed-large** | Embedding model for vector search         |
| **ChromaDB**        | Vector storage & retrieval               |
| **Django**          | Web framework & frontend                 |
| **Python**          | Core language                           |

---

---

## 🧪 Local Setup

### 1. Clone the Repo
```bash
git clone https://github.com/A7-ha4/Travell_assistant.git
cd Travell_assistant

### Set up environment 
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

### Run ollama locally
ollama run llama3:8b

### Start the server
python manage.py runserver

