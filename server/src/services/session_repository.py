import json
from pathlib import Path

import paths
from src.core.session import *

class SessionRepository:
    def __init__(self):
        self.save_directory = paths.SAVE_PATH

    def reset_session(self, session : Session):
        session.name = ''
        session.description = ''

    def save_session(self, session : Session):
        if not (Path.exists(self.save_directory)):
            self.save_directory.mkdir()
        if not (Path.exists(self.save_directory / f'{session.name}')):
            directory = self.save_directory / f'{session.name}'
            directory.mkdir()
        try:
            with open(self.save_directory / f'{session.name}' / 'session.json', 'w', encoding='utf-8') as f:
                f.write(session.model_dump_json(indent=2))
        except Exception as e:
            print("error:" + str(e))

    def load_session(self, session_name : str, session : Session):
        try:
            with open(self.save_directory / f'{session_name}' / 'session.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                session.name = data['name']
                session.description = data['description']
        except FileNotFoundError as e:
            print(str(e))
        except Exception as e:
            print(str(e))