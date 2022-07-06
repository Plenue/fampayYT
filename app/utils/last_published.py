from sqlalchemy.orm import Session
from sqlalchemy import select, func

from app.db.models.videos import Video


def get_latest_date(db: Session):
    for date in db.query(func.max(Video.date_posted)).first():
        return date
