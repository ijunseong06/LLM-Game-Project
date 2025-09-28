from src.llm import client
from src.core.config import *

async def generate_item():
    response = await client.get_client().aio.models.generate_content(
        model="gemini-2.5-flash", contents=f"Create an item object in pure JSON format, without any markdown or code blocks. Do not include escape characters. The JSON object should have three keys: 'name' (string), 'description' (string), and 'stats' (object). The 'stats' object should have the following keys: {statsKeysList}. Do not include any extra text, explanations, or code."
    )
    response_text = response.text.replace('\\"', '"')
    return response_text