import datetime
from enum import Enum
from fastapi import APIRouter, Depends

from app.db.session import get_db
from app.utils.get_videos import search_videos

router = APIRouter()


@router.get("/search")
def health(Session=Depends(get_db)):
    search_videos(Session)
    return {"Status": "Running Fine"}
