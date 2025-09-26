from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.api import game_session, llm

app = FastAPI()
app.include_router(game_session.router, prefix="/session")
app.include_router(llm.router, prefix="/llm")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)