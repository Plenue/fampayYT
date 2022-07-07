import time
import uvicorn
import threading
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers.base import api_router
from app.core.config import settings
from app.db.session import engine
from app.db.session import SessionLocal
from app.db.base import Base
from app.utils.yt_scraping import yt_scraping


tags_metadata = [
    {"name": "health check", "description": "Check Server Health",},
    {"name": "search", "description": "Search on YT DB",},
]


def yt_data():
    while True:
        Session = SessionLocal()
        yt_scraping(Session)
        time.sleep(180)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESC,
        version=settings.PROJECT_VERSION,
        openapi_tags=tags_metadata,
    )

    try:
        create_tables()
    except Exception as e:
        print("app.main: Create Table Schema in DB")
        print(e)

    try:
        t = threading.Thread(target=yt_data)
        t.start()
    except Exception as e:
        print("app.main: Thread Issue")
        print(e)

    app.include_router(api_router)
    return app


app = start_application()
