from fastapi import APIRouter, Depends

from src.core.dependencies import get_session, get_session_repo
from src.core.session import Session
from src.services.session_repository import SessionRepository

router = APIRouter()

@router.get('/get')
def get_current_session(session : Session = Depends(get_session)):
    return session

@router.post('/init')
def create_session(session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.init_session(session)

@router.post('/save')
def save_session(name : str, description : str, session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.save_session(name, description, session)

@router.post('/load')
def load_session(name_to_load : str, session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.load_session(name_to_load, session)