from pydantic import BaseModel
from typing import Literal

from src.objects.player import Player

class HistoryEntry(BaseModel):
    role: Literal['user', 'assistant']
    content : str

class Session(BaseModel):
    statsKeyList : list[str] = []

    player : Player = Player()

    history : list[HistoryEntry] = []