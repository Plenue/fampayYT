from sqlalchemy.orm import Session
from sqlalchemy import select, func

from app.db.models.videos import Video


def get_latest_date(db: Session):
    try:
        if db.query(Video).count() > 0:
            for date in db.query(func.max(Video.date_posted)).first():
                return date
        else:
            return None

    except Exception as e:
        print("app.utils.last_published: ORM Call")
        print(e)
