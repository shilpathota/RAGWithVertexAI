import os

import vertexai
from google.oauth2 import service_account
from vertexai.preview.generative_models import GenerativeModel
from dotenv import load_dotenv

load_dotenv()

def summarize_chat(chat_log: str) -> dict:
    if not chat_log:
        return {"error": "Chat log is empty"}
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    credentials = service_account.Credentials.from_service_account_file(credentials_path)

    vertexai.init(
        project=os.getenv("GOOGLE_PROJECT_ID"),
        location=os.getenv("GOOGLE_LOCATION"),
        credentials=credentials
    )
    print("Initiation successful!!")
    model = GenerativeModel("gemini-2.0-flash-lite-001")
    print("Prepared model!!")
    # Load summarization prompt
    with open("app/prompts/summarize_prompt.txt", "r") as file:
        prompt_template = file.read()

    prompt = prompt_template.replace("{{chat_log}}", chat_log)
    print("created prompt!!")
    response = model.generate_content(
        prompt
    )
    print("Response received!!")
    return {"summary": response.text}
