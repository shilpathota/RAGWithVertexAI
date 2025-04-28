import os
import vertexai
from google.oauth2 import service_account
from vertexai.preview.generative_models import GenerativeModel
from dotenv import load_dotenv

load_dotenv()

def get_vertex_model(model_name="gemini-2.0-flash-lite-001"):
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    credentials = service_account.Credentials.from_service_account_file(credentials_path)

    vertexai.init(
        project=os.getenv("GOOGLE_PROJECT_ID"),
        location=os.getenv("GOOGLE_LOCATION"),
        credentials=credentials
    )
    model = GenerativeModel(model_name)
    return model
