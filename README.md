# Enhanced RAG System: Chat Summarization + Document QA

##  Project Overview

This project started as a **Chat Summarization API** using **Vertex AI Gemini** to generate concise summaries from chat conversations.

It has now been **enhanced** to support:
- Uploading **Research Papers / Documents** 📄
- **Semantic Search** inside documents using **FAISS**
- **Natural Language Question Answering** from uploaded content

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

##  Example

1. Upload research paper: `Artificial Intelligence and Its Applications`
2. Ask: `"What is the synopsis of the paper?"`
3. Result:

> "The paper examines the features, introduction, definitions, history, applications, growth, and achievements of Artificial Intelligence across sectors like healthcare, finance, agriculture, and more."

---

##  System Architecture (Block Diagram)

![ChatGPT Image Apr 27, 2025, 09_29_35 PM](https://github.com/user-attachments/assets/e5dfc7b1-7d79-4d2e-ae63-2143c3f782f9)


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

##  API Endpoints

### 1. Upload Document
- **POST** `/upload-doc`
- **Body**: Form-Data (Key: `file`, Type: File)

### 2. Query Document
- **POST** `/query-doc`
- **Body**: JSON
```json
{
  "question": "What is the main idea of the document?"
}
```

### 3. Summarize Chat
- **POST** `/summarize-chat`
- **Body**: JSON
```json
{
  "chat_log": "Your conversation log here"
}
```

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

## ⭐️ If you find this project useful, give it a star and share it with others!

---

#AI #MachineLearning #VertexAI #FAISS #FastAPI #DocumentSummarization #ChatSummarization #Python #RAG #GitHubProject
