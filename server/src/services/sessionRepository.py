import json
import uuid

import paths
from src.core.session import *

class SessionRepository:
    def __init__(self):
        self.save_directory = paths.SAVE_PATH
        self.current_session : Session | None = None

    def create_new_session(self, session_name, session_description):
        self.current_session = Session(name=session_name, description=session_description)