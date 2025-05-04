import requests
import json
import uuid

MCP_URL = "http://127.0.0.1:8365/mcp"
MCP_UPLOAD_URL = "http://127.0.0.1:8365/mcp/upload"

def summarize_chat(chat_log: str) -> dict:
    payload = {
        "request_id": str(uuid.uuid4()),
        "context": {
            "type": "summarization",
            "data_sources": [],
            "query": chat_log
        }
    }
    response = requests.post(MCP_URL, json=payload)
    return response.json()["response"]

def ask_question(question: str, data_sources=["research_papers"]) -> dict:
    payload = {
        "request_id": str(uuid.uuid4()),
        "context": {
            "type": "doc_query",
            "data_sources": data_sources,
            "query": question
        }
    }
    response = requests.post(MCP_URL, json=payload)
    return response.json()["response"]

def upload_doc(file_path: str, source="chatbot_upload") -> dict:
    metadata = {
        "request_id": str(uuid.uuid4()),
        "context": {
            "type": "upload_doc",
            "data_sources": [],
            "query": json.dumps({"source": source})
        }
    }
    with open(file_path, "rb") as f:
        files = {
            "file": (file_path.split("/")[-1], f, "application/pdf"),
            "metadata": (None, json.dumps(metadata))
        }
        response = requests.post(MCP_UPLOAD_URL, files=files)
        return response.json()
