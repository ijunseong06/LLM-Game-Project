from pydantic import BaseModel
from typing import Optional

class Entity(BaseModel):
    name : Optional[str]
    gender : Optional[str]
    age : Optional[int]
    race : Optional[str]
    appearence : Optional[str]
    personality : Optional[str]
    background : Optional[str]
    note : Optional[str]