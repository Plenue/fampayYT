import os
import json
from dotenv import load_dotenv

from pathlib import Path

env_path = Path("./app") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Fampay's Youtuber"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESC = """Fampay's Youtuber 🚀"""

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    YT_SEARCH_QUERY: str = os.getenv("YT_SEARCH_QUERY", "phones")
    YT_API_KEY: list = json.loads(os.getenv("YT_API_KEY"))


settings = Settings()
