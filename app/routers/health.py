import datetime
from enum import Enum
from fastapi import APIRouter, Depends

from app.db.session import get_db
from app.utils.dbTest import dbStatus

router = APIRouter()


@router.get("/health")
def health(Session=Depends(get_db)):
    dbStatus(Session)
    return {"Status": "Running Fine"}
