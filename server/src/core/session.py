from pydantic import BaseModel
from typing import Optional

class Session(BaseModel):
    name : Optional[str] = None
    description : Optional[str] = None