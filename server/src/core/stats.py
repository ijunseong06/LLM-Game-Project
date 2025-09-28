from pydantic import BaseModel, Field

from src.core.config import *

class Stats(BaseModel):
    stats : dict[str, int | float] = Field(
        default_factory=lambda: {key: 0 for key in statsKeysList}
    )