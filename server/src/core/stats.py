from pydantic import BaseModel, Field

from core.config import *

class Stats(BaseModel):
    stats : dict[str, int | float] = Field(
        default_factory=lambda: {key: 0 for key in statsKeysList}
    )