from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import uvicorn

from src.api import game_session
from src.core.session import *
from src.llm.item_generater import *
import src.llm.client as client

app = FastAPI()
app.include_router(game_session.router, prefix="/session")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

client.init_client()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)