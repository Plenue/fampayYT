import datetime
from enum import Enum
from fastapi import APIRouter, Depends

from app.db.session import get_db
from app.utils.get_videos import search_videos

router = APIRouter()


@router.get("/search")
def search(Session=Depends(get_db)):
    response = search_videos(Session, query="")
    print(len(response["data"]))
    return response
