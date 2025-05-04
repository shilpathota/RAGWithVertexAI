# Enhanced RAG System: Chat Summarization + Document QA

##  Project Overview

This project started as a **Chat Summarization API** using **Vertex AI Gemini** to generate concise summaries from chat conversations.

It has now been **enhanced** to support:
- Uploading **Research Papers / Documents** 📄
- **Semantic Search** inside documents using **FAISS**
- **Natural Language Question Answering** from uploaded content

### ✅ Now MCP-Compliant!

This system has been **upgraded with MCP (Model Context Protocol)** — a standardized interface for unified interaction between the client and backend LLM services.

Built using:
- **FAISS** (Facebook AI Similarity Search) for local vector database
- **SentenceTransformer** (`all-MiniLM-L6-v2`) for embeddings
- **Vertex AI Gemini** for final answer generation
- **FastAPI** for API management
- **Postman** for API testing

---

##  Features

- Upload PDF documents.
- Generate dense embeddings using SentenceTransformer.
- Store embeddings locally in a FAISS index.
- Send natural language questions.
- Retrieve relevant document chunks via semantic search.
- Generate intelligent, human-like answers using Vertex AI Gemini.

---

## 💡 Example Flow (via MCP)

1. Upload a research paper:
   ```
   POST /mcp/upload
   ```
    - Form-Data: `file=your.pdf`
    - Metadata JSON (as `metadata` field):
      ```json
      {
        "request_id": "uuid",
        "context": {
          "type": "upload_doc",
          "data_sources": [],
          "query": "{\"source\": \"chatbot_ui\"}"
        }
      }
      ```

2. Ask a question:
   ```
   POST /mcp
   ```
   ```json
   {
     "request_id": "uuid",
     "context": {
       "type": "doc_query",
       "data_sources": ["uploaded_docs"],
       "query": "What is the methodology used in this paper?"
     }
   }
   ```

3. Summarize a chat:
   ```
   POST /mcp
   ```
   ```json
   {
     "request_id": "uuid",
     "context": {
       "type": "summarization",
       "data_sources": [],
       "query": "Customer: Hi, I have an issue...\nAgent: Can you please share your ID?"
     }
   }
   ```
---

##  System Architecture (Block Diagram)

![ChatGPT Image Apr 27, 2025, 09_29_35 PM](https://github.com/user-attachments/assets/e5dfc7b1-7d79-4d2e-ae63-2143c3f782f9)

### Updated Architecture with MCP

```
+-------------+         +---------------------+        +-----------------+
| MCP Client  |  <--->  | FastAPI MCP Server  |  --->  | Vertex AI Gemini |
+-------------+         +---------------------+        +-----------------+
       |                        |                            ↑
       |                        v                            |
       |               Semantic Search (FAISS)              |
       |                        ^                            |
       |                Document Embeddings                 |
       +-----------------+     |     +-----------------------+
                         |     v     |
                         | SentenceTransformer
                         |
                     Uploaded PDFs (pdfplumber)
```

---

##  Tech Stack

- **FastAPI** — Lightweight API framework
- **FAISS** — Vector similarity search engine
- **SentenceTransformers** — For text embeddings
- **Vertex AI Gemini** — LLM for content generation
- **pdfplumber** — For PDF text extraction
- **Postman** — API testing tool

---

##  Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/shilpathota/RAGWithVertexAI.git
cd RAGWithVertexAI
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. **Install requirements**
```bash
pip install -r requirements.txt
```

4. **Environment Variables**

Create a `.env` file:
```
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account.json
GOOGLE_PROJECT_ID=your-gcp-project-id
GOOGLE_LOCATION=your-gcp-region
```

5. **Run the API Server**
```bash
uvicorn app.main:app --port 8765 --reload
```

---

## 🔌 MCP API Endpoints

### 1. Unified Request Handling (MCP)
- `POST /mcp`
- Request:
```json
{
  "request_id": "uuid",
  "context": {
    "type": "doc_query" | "summarization",
    "data_sources": [],
    "query": "..."
  }
}
```

### 2. Document Upload (MCP)
- `POST /mcp/upload`
- Form-Data:
    - `file`: PDF file
    - `metadata`: JSON with context and source

---

##  Future Enhancements

- Document chunking for long PDFs
- Streaming response from Gemini (for long answers)
- Real-time upload and QA interface (frontend)
- Multilingual document support
- Auto Summarization of full research papers

---

##  Author

- [Linkedin](https://www.linkedin.com/in/shilpa-thota/)
- [GitHub](https://github.com/shilpathota)

---

---

#AI #MachineLearning #VertexAI #MCP #LLM #FAISS #FastAPI #DocumentSummarization #ChatSummarization #Python #RAG #GitHubProject
