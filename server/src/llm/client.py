from openai import AsyncOpenAI

client : AsyncOpenAI | None = None

from src.utils.config_loader import load_config

def get_client():
    global client
    if client == None:
        base_url = load_config()['api_server_url']
        client = AsyncOpenAI(
            base_url=base_url,
            api_key="sk-no-key-required"
            )
    return client