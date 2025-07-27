from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.environ['google_api_key']
print(google_api_key)
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai", google_api_key=google_api_key)