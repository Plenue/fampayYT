import json
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.models.videos import Video


def search_videos(db: Session):
    stmt = select(Video).order_by(Video.date_posted.desc())
    cnt = 0
    for video in db.scalars(stmt):
        cnt = cnt + 1
        v = video.__dict__
        print(str(v))
    print(cnt)
