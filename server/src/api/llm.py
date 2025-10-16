from fastapi import APIRouter, Depends
from google import genai

from src.utils.locales import Locale
from src.core.dependencies import get_session
from src.llm.client import get_client
from src.core.session import Session, HistoryEntry

router = APIRouter()

@router.post('/response/generate')
async def generate_response(input: str, client : genai.Client = Depends(get_client), session : Session = Depends(get_session)):
    system_persona = Locale.get("systemPersona")
    session_data = session.model_dump_json()
    content = [i.model_dump_json() for i in session.history] + [HistoryEntry(role="user", content=input).model_dump_json()]
    response = await client.aio.models.generate_content(
        model="gemini-2.5-flash",
        contents=content,
        config={
            "system_instruction": f"{system_persona} \n ```{session_data}```"
        }
    )
    session.history.append(HistoryEntry(role="user", content=input))
    session.history.append(HistoryEntry(role="model", content=response.text))
    return {
        "response": response.text
    }