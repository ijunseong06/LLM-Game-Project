from src.core.session import Session
from src.services.session_repository import SessionRepository

session : Session | None = None
sessionRepo : SessionRepository | None = None

def get_session():
    global session
    if session == None:
        session = Session()
    return session

def get_session_repo():
    global sessionRepo
    if sessionRepo == None:
        sessionRepo = SessionRepository()
    return sessionRepo