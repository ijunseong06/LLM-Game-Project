import uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.services.sessionRepository import *

router = APIRouter()

@router.post('/create')
def create_new_session():
    session = SessionRepository()
    return session.current_session.model_dump_json()
