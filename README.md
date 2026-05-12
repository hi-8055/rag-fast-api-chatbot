# Conversational RAG API with FastAPI

A lightweight Conversational RAG (Retrieval-Augmented Generation) system built using FastAPI, Qdrant, Redis, and Sentence Transformers.

## Features

- PDF and TXT document upload
- Text extraction from documents
- Fixed-size text chunking
- Embedding generation using Sentence Transformers
- Vector storage with Qdrant
- Conversational memory using Redis
- Semantic document retrieval
- Custom RAG prompt construction
- LLM integration using Euron API

---

## Tech Stack

- FastAPI
- Qdrant
- Redis
- Sentence Transformers
- PyMuPDF
- Docker

---

## Project Structure

```text
app/
│
├── api/
│   ├── upload.py
│   └── chat.py
│
├── services/
│   ├── chunk_service.py
│   ├── embedding_service.py
│   ├── file_service.py
│   ├── llm_service.py
│   ├── prompt_service.py
│   ├── redis_service.py
│   └── vector_service.py
│
├── models/
│   └── chat.py
│
├── uploads/
│
└── main.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/hi-8055/rag-fast-api-chatbot.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Services

### Start Qdrant

```bash
docker run -p 6333:6333 qdrant/qdrant
```

### Start Redis

```bash
docker run -p 6379:6379 redis
```

---

## Environment Variables

Create `.env` inside `app/`

```env
EURI_API_KEY=your_api_key
```

---

## Run FastAPI Server

```bash
uvicorn main:app --reload
```

Open Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Upload Document

```http
POST /files/upload
```

Supported files:
- PDF
- TXT

---

### Chat with Documents

```http
POST /chat/
```

Example Request:

```json
{
  "session_id": "session_1",
  "query": "Summarize the uploaded document"
}
```

---

## RAG Workflow

```text
Upload Document
    ↓
Extract Text
    ↓
Chunking
    ↓
Generate Embeddings
    ↓
Store in Qdrant
    ↓
User Query
    ↓
Vector Search
    ↓
Retrieve Relevant Chunks
    ↓
Build Prompt
    ↓
LLM Response
```


## License

MIT License
