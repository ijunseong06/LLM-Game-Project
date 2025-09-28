from fastapi import APIRouter, Depends
from google import genai

from src.core.dependencies import get_session
from src.llm.client import get_client
from src.core.session import Session

router = APIRouter()

@router.post('/response/generate')
async def generate_response(client : genai.Client = Depends(get_client), session : Session = Depends(get_session)):
    response = await client.aio.models.generate_content(
        model="gemini-2.5-flash", contents="Test prompt. Say anything."
    )
    session.history.append(response.text)
    return {
        "response": response.text
    }