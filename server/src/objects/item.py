from pydantic import BaseModel

from core.stats import *

class Item(BaseModel):
    name : str
    description : str
    stats : Stats