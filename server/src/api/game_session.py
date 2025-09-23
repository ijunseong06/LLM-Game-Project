from fastapi import APIRouter, Depends

from src.core.dependencies import get_session, get_session_repo
from src.core.session import Session
from src.services.session_repository import SessionRepository

router = APIRouter()

@router.get('/get')
def get_current_session(session : Session = Depends(get_session)):
    return session

@router.post('/create')
def create_session(name : str, desc : str, session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.reset_session(session)
    session.name = name
    session.description = desc
    return {"name" : session.name, "description": session.description}

@router.post('/save')
def save_session(session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.save_session(session)

@router.post('/load')
def load_session(name_to_load : str, session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.load_session(name_to_load, session)