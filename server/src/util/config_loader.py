import os
import json

import paths

initial_config = {
    "GEMINI_API_KEY": None
}

if not os.path.exists(os.path.join(paths.BASE_DIR, 'config.json')):
    print("config.json is not exists. Create a new file.")
    with open(os.path.join(paths.BASE_DIR, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump(initial_config, f, indent=2)

def load_config():
    try:
        with open(os.path.join(paths.BASE_DIR, 'config.json'), 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config
    except Exception as e:
        print("error occured on load config.json.")
        return initial_config