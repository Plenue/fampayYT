from fastapi import APIRouter

from app.routers import health
from app.routers import search


api_router = APIRouter()
api_router.include_router(health.router, tags=["health check"])
api_router.include_router(search.router, tags=["search"])
