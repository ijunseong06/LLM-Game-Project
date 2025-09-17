from fastapi import APIRouter, Depends

import paths
from src.core.dependencies import get_session, get_session_repo
from src.core.session import Session
from src.services.session_repository import SessionRepository

router = APIRouter()

@router.get('/get')
def get_current_session(session : Session = Depends(get_session)):
    return session

@router.post('/save')
def save_session(session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.save_session(session)