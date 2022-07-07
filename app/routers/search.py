import datetime
from enum import Enum
from fastapi import APIRouter, HTTPException, Query, Depends

from app.db.session import get_db
from app.utils.get_videos import search_videos

router = APIRouter()

# Update Status Code
@router.get("/video/search")
def search(
    per_page_count: int,
    page_no: int,
    query: str = Query(default="", min_length=0),
    Session=Depends(get_db),
):
    if per_page_count < 5:
        raise HTTPException(
            status_code=400,
            detail="app.routers.search: Per Page Count less than to 5.",
        )
    elif page_no <= 0:
        raise HTTPException(
            status_code=400,
            detail="app.routers.search: Page Number less than or equal to 0.",
        )

    try:
        response = search_videos(query, per_page_count, page_no, Session)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="app.routers.search: Error while executing search_videos.",
            headers={"X-Error": e},
        )
    if response["status"] == "Failed":
        raise HTTPException(
            status_code=400, detail="app.routers.search: " + response["message"],
        )

    print(str(len(response["data"])) + " Retured to API.")
    return response
