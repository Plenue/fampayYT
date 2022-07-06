import datetime
from enum import Enum
from fastapi import APIRouter, Depends, HTTPException

from app.db.session import get_db
from app.utils.get_videos import search_videos

router = APIRouter()


@router.get("/search")
def search(query: str, Session=Depends(get_db)):
    try:
        response = search_videos("car test", Session)
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail="app.routers.search: Error while executing search_videos.",
            headers={"X-Error": e},
        )

    print(len(response["data"]))
    return response
