from pydantic import BaseModel
from typing import Optional

from src.objects.player import Player

class Session(BaseModel):
    player : Player = Player()

    history : list[str] = []