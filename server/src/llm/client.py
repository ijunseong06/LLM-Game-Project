from google import genai

from src.utils import config_loader

client : genai.Client | None = None

def get_client():
    global client
    if client == None:
        config = config_loader.load_config()
        api_key = config['GEMINI_API_KEY']
        client = genai.Client(api_key=api_key)
    return client