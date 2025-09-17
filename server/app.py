from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import uvicorn

from server.src.api import game_session
from src.core.session import *
from src.llm.item_generater import *
import src.llm.client as client

app = FastAPI()
app.include_router(game_session)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/api/data')
async def create_item():
    try:
        item_text = await generate_item()
        return json.loads(item_text)
    except json.JSONDecodeError:
        return {"error": "Response of AI is not valid JSON format"}
    except Exception as e:
        return {"error": str(e)}


client.init_client()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)