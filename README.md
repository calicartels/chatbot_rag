# Multimodal RAG Chatbot System

## Overview

This repo is a full-stack, multimodal Retrieval-Augmented Generation (RAG) chatbot system. It supports document upload, chunking, embedding, retrieval, and answer generation for both text and images. The system is modular, production-ready, and integrates with Google Vertex AI for embeddings.

**Key Components:**
- **Streamlit App**: Upload, index, and query documents (PDFs, images, etc.)
- **FastAPI Backend**: API for RAG operations, document indexing, and chat
- **React/Vite Frontend**: (Optional) Modern web UI
- **Modular RAG Pipeline**: Extraction, embedding, retrieval, and generation

---

## Demo Video & Live App

[![Watch the video](https://img.youtube.com/vi/eKd9_d1zaoY/0.jpg)](https://www.youtube.com/watch?v=eKd9_d1zaoY&ab_channel=VishnuMukundan)

👉 [Try the Streamlit app live](https://calicartels-assignment-llms-3-streamlit-app-h15fc7.streamlit.app/)

---

## Features
- **Multimodal**: Handles both text and image evidence from PDFs
- **RAG Pipeline**: Extraction, chunking, embedding, retrieval, and answer generation
- **Google Vertex AI**: For embedding and model inference (configurable)
- **Chunking**: Smart chunking of text and images for better retrieval
- **Evidence**: Answers are supported by both text and image evidence
- **API-first**: FastAPI backend for programmatic access
- **Modern UI**: Streamlit and React frontends
- **Credential isolation**: All secrets/keys are gitignored

---

## Directory Structure
```
chatbot_rag/
├── backend/                  # FastAPI backend, document indexing, API
│   ├── api/                  # FastAPI app and routes
│   ├── config/               # Backend config (host, port, etc.)
│   ├── rag/                  # RAG pipeline: document store, retriever, generator
│   ├── utils/                # Auth, Google integration, doc processing
│   ├── main.py               # Backend entry point (indexing, API launch)
│   └── requirements.txt      # Backend Python deps
├── credentials/              # Google Cloud credentials (gitignored)
├── data/                     # Uploaded/processed PDFs (gitignored)
├── static/                   # Indexed data, images, etc. (gitignored)
│   ├── index/                # Saved vector indices
│   ├── images/               # Extracted images
│   └── text/                 # Extracted text chunks
├── modules/                  # Core RAG logic (extraction, embedding, retrieval, generation)
├── utils/                    # Shared utilities
├── frontend/                 # React/Vite frontend (optional)
│   ├── src/                  # React source code
│   ├── public/               # Static assets
│   ├── package.json          # Frontend deps
│   └── vite.config.ts        # Vite config
├── streamlit_app.py          # Streamlit UI (main entry for most users)
├── requirements.txt          # Python deps for root/Streamlit
├── .gitignore                # Ignores secrets, venv, junk
├── README.md                 # This file
└── My Movie.mp4              # Demo video (local)
```

---

## Technical Details

### Multimodal RAG Pipeline
- **Extraction**: Parses PDFs, extracts both text and images
- **Chunking**: Splits text into overlapping or semantic chunks; images are chunked by page/region
- **Embedding**: Uses Google Vertex AI (or local models) to embed both text and image chunks
- **Indexing**: Saves embeddings and metadata to `static/index/` as JSON
- **Retrieval**: At query time, retrieves top-k relevant chunks (text and images) using vector similarity
- **Generation**: Uses a language model (Vertex AI or OpenAI, configurable) to synthesize answers, citing both text and image evidence

### Models Used
- **Embeddings**: Google Vertex AI embedding models (can swap for OpenAI or local models)
- **Generation**: Vertex AI LLMs (e.g., PaLM, Gemini), or OpenAI GPT-3.5/4 (configurable)
- **Image Handling**: PIL for image extraction, storage, and display

### Config & Credentials
- All sensitive keys in `credentials/` (never committed)
- Backend config in `backend/config/settings.py` (host, port, doc IDs, model selection)
- Streamlit and backend both support local and cloud operation

### API Endpoints (FastAPI)
- `/api/chat` — Query the RAG system (POST)
- `/api/index-document` — Index a new document (POST)
- `/health` — Health check (GET)

---

## Quickstart

### 1. Clone and Install
```bash
git clone <your_repo_url>
cd chatbot_rag
```

### 2. Python Backend/API
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# To index docs:
python main.py --index
# To run API:
python main.py --run-api
```

### 3. Streamlit App (Recommended)
```bash
cd ..
streamlit run streamlit_app.py
```

### 4. React Frontend (Optional)
```bash
cd frontend
npm install
npm run dev
```

---

## How it Works
1. **Upload**: User uploads a PDF (via Streamlit or API)
2. **Extraction**: Text and images are extracted and chunked
3. **Embedding**: Chunks are embedded (Vertex AI or local)
4. **Indexing**: Indexed data saved to `static/index/`
5. **Query**: User asks a question; system retrieves relevant chunks and generates an answer
6. **Evidence**: Answers are supported by text/image evidence

---

## Troubleshooting
- If you get auth errors, check your credentials in `credentials/`
- If you see missing index errors, process a document first
- For frontend/backend API issues, make sure both are running and ports match
- For model/config issues, check `backend/config/settings.py`

---

## License
MIT License

---

## Credits
Built by Vishnu Mukundan. Powered by OpenAI, Google Vertex AI, Streamlit, FastAPI, React, Vite.