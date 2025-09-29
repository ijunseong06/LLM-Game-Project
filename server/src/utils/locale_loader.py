import json

import paths

def load_locale(lang_code : str):
    with open(paths.BASE_PATH / 'locales' / f'{lang_code}.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        return json_data