from google import genai

from ..utils import config_loader

client : genai.Client = None

def api_key_exists():
    config = config_loader.load_config()
    if (config['GEMINI_API_KEY']):
        return True
    else:
        return False

def init_client():
    global client
    if api_key_exists():
        config = config_loader.load_config()
        api_key = config['GEMINI_API_KEY']
        if client == None:
            client = genai.Client(api_key=api_key)

def get_client():
    global client
    return client