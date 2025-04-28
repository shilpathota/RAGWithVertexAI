from fastapi import FastAPI, Request, UploadFile, File  # ← add File here
from app.summarizer import summarize_chat
from fastapi import UploadFile, File
from app.doc_ingestion import ingest_document, query_documents
import os

from app.utils.vertex_model import get_vertex_model

app = FastAPI()
@app.get("/")
def root():
    print("Root endpoint hit")
    return {"message": "It works!"}

@app.post("/summarize-chat")
async def summarize_chat_endpoint(request: Request):
    data = await request.json()
    print(data)
    return summarize_chat(data.get("chat_log", ""))


@app.post("/upload-doc")
async def upload_doc(file: UploadFile = File(...)):
    upload_dir = "data/uploaded_docs"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    metadata = {"filename": file.filename}
    result = ingest_document(file_path, metadata)
    return result

@app.post("/query-doc")
async def query_doc_endpoint(request: Request):
    data = await request.json()
    question = data.get("question", "")
    retrieved_docs = query_documents(question)

    if not retrieved_docs:
        return {"answer": "No documents found. Please upload documents first before querying."}

    with open("app/prompts/doc_qa_prompt.txt", "r") as file:
        prompt_template = file.read()

    prompt = prompt_template.replace("{{retrieved_docs}}", "\n\n".join(retrieved_docs)).replace("{{question}}", question)

    model = get_vertex_model()
    response = model.generate_content(prompt)

    return {"answer": response.text}