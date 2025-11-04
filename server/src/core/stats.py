from pydantic import BaseModel, Field

from src.core.dependencies import get_session

class Stats(BaseModel):
    stats : dict[str, int | float] = Field(
        default_factory=lambda: {key: 0 for key in get_session().statsKeyList}
    )