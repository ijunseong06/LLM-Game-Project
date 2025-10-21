from fastapi import APIRouter, Depends
from openai import AsyncOpenAI

from src.core.session import Session
from src.core.dependencies import get_session
from src.llm.client import get_client
from src.llm.response import Response

router = APIRouter()

@router.post('/response/generate')
async def get_response(input: str, client : AsyncOpenAI = Depends(get_client), session : Session = Depends(get_session)):
    return await Response.generate_story(input, client, session)