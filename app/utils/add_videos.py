from sqlalchemy.orm import Session

from app.schemas.videos import VideoCreate
from app.db.models.videos import Video


def add_new_videos(video, db: Session):
    try:
        videoEntry = Video(
            title=video["title"],
            channel_name=video["channel_name"],
            url=video["url"],
            description=video["description"],
            date_posted=video["date_posted"],
        )
        db.add(videoEntry)
        db.commit()
        db.refresh(videoEntry)
        return videoEntry

    except Exception as e:
        print("app.utils.add_videos: ORM Data Push Call")
        print(e)
