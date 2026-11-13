import os
from dotenv import load_dotenv

load_dotenv()


def _bool(name: str, default: bool = False) -> bool:
    return os.getenv(name, str(default)).strip().lower() in ("1", "true", "yes")


BASE_URL = os.getenv("BASE_URL", "")
LOGIN_URL = os.getenv("LOGIN_URL", BASE_URL)
USERNAME = os.getenv("APP_USERNAME", "")
PASSWORD = os.getenv("APP_PASSWORD", "")
HEADLESS = _bool("HEADLESS")
SLOW_MO = int(os.getenv("SLOW_MO", "0"))
TIMEOUT_MS = int(os.getenv("TIMEOUT_MS", "30000"))
