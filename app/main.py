import uvicorn
from fastapi import FastAPI

from app.routers.base import api_router
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

tags_metadata = [
    {"name": "health check", "description": "Check Server Health",},
]


def create_tables():
    print("Creating Tables")
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESC,
        version=settings.PROJECT_VERSION,
        openapi_tags=tags_metadata,
    )
    create_tables()
    app.include_router(api_router)
    return app


app = start_application()
