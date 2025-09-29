from enum import Enum
import locale

from src.utils.locale_loader import load_locale

LOCALE_MAPPING = {
    "ko-KR": "KR",
    "en-US": "en"
}

class Locales(Enum):
    KR = load_locale('ko-KR')
    EN = load_locale('en-US')

class Locale:
    def get(key : str):
        current_locale = locale.getlocale()
        return Locales[LOCALE_MAPPING.get(current_locale, "EN")].value[f'{key}']