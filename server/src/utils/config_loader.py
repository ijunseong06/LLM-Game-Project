from pathlib import Path
import json

import paths

initial_config = {
    "GEMINI_API_KEY": None
}

if not Path.exists(paths.BASE_PATH / 'config.json'):
    print("config.json is not exists. Create a new file.")
    with open(paths.BASE_PATH / 'config.json', 'w', encoding='utf-8') as f:
        json.dump(initial_config, f, indent=2)

def load_config():
    try:
        with open(paths.BASE_PATH / 'config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config
    except Exception:
        print("error occured on load config.json.")
        return initial_config