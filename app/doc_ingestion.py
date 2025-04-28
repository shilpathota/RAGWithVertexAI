# app/doc_ingestion.py
import os
import uuid
import pickle
import pdfplumber
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# === Settings ===
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
UPLOAD_DIR = "data/uploaded_docs"
VECTOR_DB_PATH = "data/vector_db/index.faiss"
METADATA_DB_PATH = "data/vector_db/metadata.pkl"

# === Global Variables ===
embedding_model = SentenceTransformer(EMBEDDING_MODEL)
index = None
metadata_store = {}

# === Initialize FAISS Index ===
def initialize_faiss():
    global index, metadata_store
    os.makedirs(os.path.dirname(VECTOR_DB_PATH), exist_ok=True)

    embedding_size = embedding_model.get_sentence_embedding_dimension()

    if os.path.exists(VECTOR_DB_PATH):
        print("Loading existing FAISS index...")
        index = faiss.read_index(VECTOR_DB_PATH)
        if os.path.exists(METADATA_DB_PATH):
            with open(METADATA_DB_PATH, "rb") as f:
                metadata_store = pickle.load(f)
    else:
        print("Creating new FAISS index...")
        index = faiss.IndexFlatL2(embedding_size)
        metadata_store = {}

# === PDF Text Extraction ===
def extract_text_from_pdf(pdf_path: str) -> str:
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

# === Ingest Document ===
def ingest_document(file_path: str, metadata: dict = {}):
    initialize_faiss()

    doc_id = str(uuid.uuid4())
    content = extract_text_from_pdf(file_path)

    # Create embedding
    embedding = embedding_model.encode([content])[0]  # (1, dim)
    embedding = np.array(embedding).astype("float32").reshape(1, -1)

    # Add to FAISS
    index.add(embedding)
    metadata_store[len(metadata_store)] = {"doc_id": doc_id, "content": content, **metadata}

    # Save
    faiss.write_index(index, VECTOR_DB_PATH)
    with open(METADATA_DB_PATH, "wb") as f:
        pickle.dump(metadata_store, f)

    return {"doc_id": doc_id, "status": "success", "metadata": metadata}

# === Query Documents ===
def query_documents(question: str, top_k: int = 3):
    initialize_faiss()

    if index.ntotal == 0:
        return []

    # Embed query
    query_embedding = embedding_model.encode([question])[0]
    query_embedding = np.array(query_embedding).astype("float32").reshape(1, -1)

    # Search
    distances, indices = index.search(query_embedding, top_k)

    retrieved_docs = []
    for idx in indices[0]:
        if idx in metadata_store:
            retrieved_docs.append(metadata_store[idx]["content"])

    return retrieved_docs
