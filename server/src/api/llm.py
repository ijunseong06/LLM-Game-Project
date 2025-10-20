from fastapi import APIRouter, Depends
from openai import AsyncOpenAI

from src.utils.locales import Locale
from src.utils.config_loader import load_config
from src.core.dependencies import get_session
from src.llm.client import get_client
from src.core.session import Session, HistoryEntry

router = APIRouter()

@router.post('/response/generate')
async def generate_response(input: str, client : AsyncOpenAI = Depends(get_client), session : Session = Depends(get_session)):
    persona = Locale.get('persona')
    session_data = session.model_dump_json()
    # ---
    # 프롬프트 구성
    # ---
    #
    # 역할
    # 현재 세션 데이터
    system_prompt = (
        f"# {Locale.get('role')} \n\n" +
        persona +
        f"\n\n# {Locale.get('sessionData')}\n\n"
        "```json\n"
        f"{session_data}"
        "\n```"
    )
    history = [i.model_dump() for i in session.history]
    user_input = HistoryEntry(role="user", content=input).model_dump()
    response = await client.chat.completions.create(
        model=load_config()['model_name'],
        messages=[
            {
                'role': 'system',
                'content': f'{system_prompt}'
            }
        ] +
        history +
        [user_input]
    )
    session.history.append(HistoryEntry(role="user", content=input))
    session.history.append(HistoryEntry(role="assistant", content=response.choices[0].message.content))
    return {
        "response": response.choices[0].message.content
    }