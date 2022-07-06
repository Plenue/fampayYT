import datetime
from enum import Enum
from fastapi import APIRouter, Depends

from app.db.session import get_db
from app.utils.db_test import db_status

router = APIRouter()


@router.get("/health")
def health(Session=Depends(get_db)):
    db_status(Session)
    return {"Status": "Running Fine"}
