from fastapi import APIRouter, Depends
from google import genai

from src.core.dependencies import get_session, get_session_repo
from src.llm import client

router = APIRouter()

@router.get('/get')
async def create_response(client : genai.Client = Depends(client.get_client)):
    response = await client.aio.models.generate_content(
        model="gemini-2.5-flash", contents="Test prompt. Say anything."
    )
    return {
        "response": response.text
    }