# Full-Stack RAG App

A full-stack Retrieval-Augmented Generation application built from scratch. Upload documents (PDF, DOCX, TXT, CSV), and ask questions against them — powered by local embeddings and Claude.

> **Built intentionally.** Every file, every dependency, and every architectural decision in this project was made with intent. No vibe coding.

---

## How It Works

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Upload a  │ ──▶ │  Parse &    │ ──▶│  Chunk &    │
│   Document  │     │  Extract    │     │  Embed      │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Answer    │ ◀──│  Generate   │ ◀── │  Retrieve   │
│   Displayed │     │  via Claude │     │  from Store │
└─────────────┘     └─────────────┘     └─────────────┘
```

1. **Parse** — Extract plain text from uploaded files (PDF, DOCX, TXT, CSV)
2. **Chunk** — Split text into overlapping segments sized for embedding
3. **Embed** — Convert chunks into vector representations using a local model
4. **Store** — Save embeddings in a local vector database for fast retrieval
5. **Retrieve** — When a question is asked, find the most relevant chunks by semantic similarity
6. **Generate** — Send the retrieved chunks + question to Claude, get a grounded answer back

---

## Tech Stack

| Layer       | Technology                          | Runs Where |
|-------------|-------------------------------------|------------|
| Frontend    | React JS                            | Netlify    |
| Backend API | Python / FastAPI                    | Render     |
| Embeddings  | sentence-transformers (MiniLM-L6-v2)| Local      |
| Vector Store| ChromaDB                            | Local      |
| LLM         | Anthropic API (Claude)              | API call   |

The only external API call in the entire app is to Claude for answer generation. Everything else runs locally.

---

## Project Structure

```
rag-app/
├── backend/
│   ├── config.py          # API keys, model names, chunk sizes — one place to tune everything
│   ├── parsers.py         # Turns raw files into plain text
│   ├── chunker.py         # Splits text into overlapping chunks
│   ├── embeddings.py      # Converts text chunks into vectors (local model)
│   ├── vector_store.py    # Stores and searches embeddings via ChromaDB
│   ├── generator.py       # Builds prompts, calls Claude, returns answers
│   ├── pipeline.py        # Wires ingestion + retrieval + generation together
│   ├── api.py             # FastAPI endpoints for upload and question answering
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## Features

- **Document chat** — Upload a file and ask questions about its contents
- **Multi-format support** — PDF, DOCX, TXT, and CSV
- **Pre-loaded demo docs** — Browse and query example documents without uploading anything
- **Visitor uploads** — Upload your own files (size and count limits apply)
- **Rate-limited API** — Usage caps to keep costs manageable

---

## Build Phases

This project was built in 10 sequential phases. Each phase was completed and tested before moving to the next.

### Phase 1 — Project Setup & Configuration
Set up the repo structure, virtual environment, `requirements.txt`, and `config.py`. Every dependency understood before installing. Backend/frontend split established from the start.

### Phase 2 — File Parsing
Built `parsers.py`. Takes in PDF, DOCX, TXT, and CSV files and outputs plain text. No AI involved — just file I/O and libraries.

### Phase 3 — Chunking
Built `chunker.py`. Takes plain text and splits it into overlapping chunks. Chunk size and overlap tuned for retrieval quality.

### Phase 4 — Embeddings
Built `embeddings.py` using sentence-transformers locally. Converts chunks into vectors. Tested by verifying that semantically similar sentences produce similar vectors.

### Phase 5 — Vector Store
Built `vector_store.py` using ChromaDB. Stores embedded chunks and queries them by similarity. At this point: feed in a document, ask a question, get back the most relevant chunks — no LLM yet.

### Phase 6 — Generation
Built `generator.py`. Takes retrieved chunks, constructs a prompt, calls the Anthropic API, and returns a grounded answer. This is where the app starts talking back.

### Phase 7 — Pipeline
Built `pipeline.py`. Wired Phases 2–6 into a clean interface: `ingest(file)` and `ask(question)`. Tested end-to-end via CLI.

### Phase 8 — Backend API
Built `api.py` using FastAPI. Exposed endpoints for file upload/ingestion and question answering. Deployed to Render.

### Phase 9 — Frontend
Built the React app — file upload area, chat interface, clean design. Connected to the backend API. Deployed to Netlify.

### Phase 10 — Polish & Portfolio
Error handling, loading states, rate limiting, and UI refinements. Written to be understood and explained, not just shown.

---

## Packages

### fastapi 
Your web framework. It handles HTTP requests (file uploads, question-asking) and turns your Python functions into API endpoints. Used in Phase 8.

### uvicorn 
The server that actually runs FastAPI. FastAPI defines your routes; uvicorn listens on a port and serves them. Think of FastAPI as the blueprint and uvicorn as the construction crew.

### python-multipart 
Required by FastAPI for handling file uploads. Without it, FastAPI can't parse multipart/form-data requests (which is how browsers send files).

### anthropic 
The official Python SDK for calling the Claude API. This is the only external AI call in your app. Used in Phase 6.

### sentence-transformers 
Runs the embedding model (all-MiniLM-L6-v2) locally on your machine. It converts text into vectors - no API call needed. Used in Phase 4.

### chromadb 
A lightweight vector database. It stores your embeddings and lets you search them by similarity. Used in Phase 5.

### pypdf2 
Extracts text from PDF files. Used in Phase 2.

### python-docx 
Extracts text from Word (.docx) files. Used in Phase 2.

### python-dotenv 
Loads environment variables from a .env file so you don't hardcode your API key. Used in this phase and throughout.

---

## Running Locally

### Backend
```
cd backend
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
<!-- uvicorn api:app --reload -->
```

### Frontend
```
cd frontend
npm install
npm start
```

Create a `.env` file in `/backend` with your Anthropic API key:
```
ANTHROPIC_API_KEY=your-key-here
```

---

## What I Learned

This project was built to understand RAG from the ground up — not just to ship a working app, but to be able to open any file and explain exactly what it does and why it's there. source venv/Scripts/activate is used to activate my virtual environment. 