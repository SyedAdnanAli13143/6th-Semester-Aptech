# 📄 Virtual Advisor — Tax Document Q&A Chatbot

A **Streamlit-based chatbot** that answers questions about tax documents using **RAG (Retrieval-Augmented Generation)**. It runs **100% locally** — no API keys, no cloud services, no data leaves your machine.

Powered by **LLaMA 3.2** (via Ollama) + **FAISS** vector search + **HuggingFace** embeddings.

---

## 📸 Features

- **PDF Document Q&A** — Upload a tax document and ask questions in natural language
- **RAG Pipeline** — Retrieves relevant document sections before generating answers
- **Fully Local** — All processing happens on your machine (Ollama + HuggingFace)
- **Chat Interface** — Conversational UI with message history
- **One-Click Clear** — Reset the conversation from the sidebar

---

## 🏗️ Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   PDF File  │────▶│  Text Extraction │────▶│  Text Chunking  │
│  (.pdf)     │     │   (PyPDF2)       │     │  (LangChain)    │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                      │
                                                      ▼
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  User Query │────▶│ Similarity Search │◀───│  FAISS Vector   │
│             │     │  (Top 3 chunks)  │     │  Store          │
└─────────────┘     └────────┬─────────┘     │  (HuggingFace   │
                             │               │   Embeddings)   │
                             ▼               └─────────────────┘
                    ┌──────────────────┐
                    │  LLaMA 3.2 via   │
                    │  Ollama (local)  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  AI Response     │
                    │  displayed in    │
                    │  Streamlit chat  │
                    └──────────────────┘
```

---

## 📋 Prerequisites

| Requirement | Version | Purpose |
|---|---|---|
| **Python** | 3.9+ | Runtime |
| **Ollama** | Latest | Local LLM server |
| **LLaMA 3.2** | (via Ollama) | Language model |

---

## 🚀 Setup & Installation

### 1. Install Ollama

Download and install from [ollama.com](https://ollama.com), then pull the model:

```bash
ollama pull llama3.2
```

Verify it's running:

```bash
ollama list
# Should show llama3.2 in the list
```

### 2. Clone the Repository

```bash
git clone <your-repo-url>
cd Virtual_Advisor
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Your PDF Document

Place your tax PDF file in the project root directory. The default expected filename is:

```
CT-Returns-EN-11-11-2024.pdf
```

To use a different PDF, update the `PDF_FILE` variable in `app.py`.

### 6. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at **http://localhost:8501**.

---

## 📁 Project Structure

```
Virtual_Advisor/
├── app.py                          # Main application (single file)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── CT-Returns-EN-11-11-2024.pdf    # Tax document (PDF)
└── venv/                           # Python virtual environment
```

---

## 🔧 Configuration

You can customize the following in `app.py`:

| Variable | Default | Description |
|---|---|---|
| `PDF_FILE` | `CT-Returns-EN-11-11-2024.pdf` | PDF document to load |
| `SYSTEM_PROMPT` | Tax advisor persona | Controls AI behavior and tone |
| `model` (in `get_ai_response`) | `llama3.2` | Ollama model to use |
| `chunk_size` | `2500` | Characters per text chunk |
| `chunk_overlap` | `350` | Overlap between chunks |
| `k` (in retriever) | `3` | Number of chunks retrieved per query |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `requests` | HTTP client for Ollama API |
| `PyPDF2` | PDF text extraction |
| `langchain` | RAG pipeline orchestration |
| `langchain-community` | FAISS vector store integration |
| `langchain-huggingface` | HuggingFace embeddings wrapper |
| `faiss-cpu` | Fast similarity search |
| `sentence-transformers` | Embedding model (`all-MiniLM-L12-v2`) |

---

## ❓ Troubleshooting

| Problem | Solution |
|---|---|
| `Ollama is not running!` | Start Ollama: `ollama serve` |
| `PDF not found` | Ensure the PDF is in the same directory as `app.py` |
| `ModuleNotFoundError` | Activate venv and run `pip install -r requirements.txt` |
| Slow first response | The embedding model downloads on first run (~50MB) |
| Out of memory | Use a smaller model: change `llama3.2` to `llama3.2:1b` |

---

## 📝 How It Works (Step by Step)

1. **PDF Ingestion** — On startup, `PyPDF2` extracts all text from the PDF document.
2. **Text Chunking** — `RecursiveCharacterTextSplitter` breaks the text into overlapping chunks of 2500 characters (350 char overlap) to preserve context at boundaries.
3. **Embedding** — Each chunk is converted into a numerical vector using the `all-MiniLM-L12-v2` model from HuggingFace (runs locally).
4. **Indexing** — Vectors are stored in a FAISS index for fast nearest-neighbor search.
5. **User Query** — When you type a question, it's also converted to a vector.
6. **Retrieval** — FAISS finds the 3 most similar chunks to your question.
7. **Augmented Prompt** — The retrieved chunks + your question are combined into a prompt.
8. **Generation** — The prompt is sent to LLaMA 3.2 via Ollama's local API.
9. **Response** — The AI's answer is displayed in the Streamlit chat interface.

---

## 🛡️ Privacy

All data stays on your machine:
- The PDF is processed locally
- Embeddings are generated locally (HuggingFace model runs on your CPU)
- LLM inference runs locally via Ollama
- No data is sent to any external API or cloud service
