import json
from pathlib import Path
import os

import paths
from src.core.session import *

class SessionRepository:
    def __init__(self):
        self.save_directory = paths.SAVE_PATH

    def init_session(self, session : Session):
        session.player = Player()
        session.history = []
    
    def get_session_list(self):
        file_list = []
        if not (Path.exists(self.save_directory)):
            self.save_directory.mkdir()
        for i in os.listdir(self.save_directory):
            try:
                with open(self.save_directory / Path(i) / 'session.json', 'r', encoding='utf-8') as f:
                    file_list.append(json.load(f))
            except:
                continue
        return file_list

    def save_session(self, name : str, description : str, session : Session):
        if not (Path.exists(self.save_directory)):
            self.save_directory.mkdir()
        if not (Path.exists(self.save_directory / f'{name}')):
            directory = self.save_directory / f'{name}'
            directory.mkdir()
        metadata = {
            "name": name,
            "description": description
        }
        try:
            with open(self.save_directory / f'{name}' / 'session.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(metadata, indent=2, ensure_ascii=False))
            with open(self.save_directory / f'{name}' / 'player.json', 'w', encoding='utf-8') as f:
                f.write(session.model_dump_json(indent=2, include={'player'}))
            with open(self.save_directory / f'{name}' / 'chat_history.json', 'w', encoding='utf-8') as f:
                f.write(session.model_dump_json(indent=2, include={'history'}))
        except Exception as e:
            print("error:" + str(e))

    def load_session(self, session_name : str, session : Session):
        try:
            with open(self.save_directory / f'{session_name}' / 'chat_history.json', 'r', encoding='utf-8') as f:
                session.history = [HistoryEntry.model_validate(i) for i in json.load(f)['history']]
            with open(self.save_directory / f'{session_name}' / 'player.json', 'r', encoding='utf-8') as f:
                session.player = Player.model_validate(json.load(f)['player'])
        except FileNotFoundError as e:
            print(str(e))
        except Exception as e:
            print(str(e))