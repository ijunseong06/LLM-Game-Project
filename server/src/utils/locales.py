from enum import Enum
from src.utils.config_loader import load_config

from src.utils.locale_loader import load_locale

LOCALE_MAPPING = {
    "ko_KR": "KR",
    "en_US": "en"
}

class Locales(Enum):
    KR = load_locale('ko_KR')
    EN = load_locale('en_US')

class Locale:
    def get(key : str):
        current_locale = load_config()["lang"]
        return Locales[LOCALE_MAPPING.get(current_locale, "EN")].value[f'{key}']