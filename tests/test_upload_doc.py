import requests

URL = "http://localhost:8765/upload-doc"

# Path to a sample PDF you want to upload
file_path = "C:\Projects\VertexAIRAG\ChatSummarization\chat-summarization\data\\researchpaper1.pdf"  # Make sure you have a test PDF here!

# Open the file in binary mode
with open(file_path, "rb") as f:
    files = {"file": (file_path, f, "application/pdf")}
    response = requests.post(URL, files=files)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())