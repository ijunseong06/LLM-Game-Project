from fastapi import APIRouter, Depends

from src.core.dependencies import get_session, get_session_repo
from src.core.session import Session
from src.services.session_repository import SessionRepository

router = APIRouter()

@router.get('/get')
def get_current_session(session : Session = Depends(get_session)):
    return session

@router.get('/get/saves')
def get_saves(repo : SessionRepository = Depends(get_session_repo)):
    return repo.get_session_list()

@router.post('/init')
def create_session(name : str, description : str, session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.init_session(session)
    repo.save_session(name=name, description=description, session=session)

@router.post('/save')
def save_session(name : str, description : str, session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.save_session(name, description, session)

@router.post('/save/player')
def save_player(name : str, gender : str, age : int, race : str, appearence : str, session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    session.player.name = name
    session.player.gender = gender
    session.player.age = age
    session.player.race = race
    session.player.appearence = appearence

@router.post('/load')
def load_session(name : str, session : Session = Depends(get_session), repo : SessionRepository = Depends(get_session_repo)):
    repo.load_session(name, session)