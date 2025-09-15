import uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core.session import active_sessions, GameSession

router = APIRouter()