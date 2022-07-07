import datetime
from enum import Enum
from fastapi import APIRouter, HTTPException

from app.utils.db_test import db_status

router = APIRouter()

# Update Status Code
@router.get("/health")
def health():
    try:
        db_status()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="app.routers.health: Error while executing db_status.",
            headers={"X-Error": e},
        )
    return {"Status": "DB Connected and Running Fine."}
