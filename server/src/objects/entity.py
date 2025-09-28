from pydantic import BaseModel
from typing import Optional

class Entity(BaseModel):
    name : Optional[str] = None
    gender : Optional[str] = None
    age : Optional[int] = None
    race : Optional[str] = None
    appearence : Optional[str] = None
    personality : Optional[str] = None
    background : Optional[str] = None
    note : Optional[str] = None