import json
import requests

URL = "http://localhost:8765/query-doc"

payload = {
    "question": "What is the main idea of the uploaded documents?"
}

response = requests.post(URL, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
