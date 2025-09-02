from google import genai

from ..core.config import *

client = genai.Client()

async def generate_item():
    response = await client.aio.models.generate_content(
        model="gemini-2.5-flash", contents=f"Create An Item. Return in dict. Item object has name, descritpion, stats. Keys of item stats : {statsKeysList}"
    )
    return response