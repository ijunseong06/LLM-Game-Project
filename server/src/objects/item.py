from pydantic import BaseModel

from src.core.stats import *

class Item(BaseModel):
    name : str
    description : str
    stats : Stats