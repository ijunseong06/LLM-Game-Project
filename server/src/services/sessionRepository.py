import json
from pathlib import Path

import paths
from src.core.session import *

class SessionRepository:
    def __init__(self):
        self.save_directory = paths.SAVE_PATH
        self.current_session : Session | None = None

    def create_new_session(self, session_name, session_description):
        self.current_session = Session(name=session_name, description=session_description)

    def save_session(self):
        if not (Path.exists(self.save_directory)):
            self.save_directory.mkdir(self.current_session.name)
        try:
            with open(self.save_directory / f'{self.current_session.name}' / 'session.json', 'w', encoding='utf-8') as f:
                json.dump(self.current_session.model_dump_json(), f, indent=2)
        except Exception as e:
            print("error:" + str(e))
