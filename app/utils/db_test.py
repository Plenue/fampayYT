from sqlalchemy.orm import Session

from app.schemas.videos import VideoCreate
from app.db.models.videos import Video


def db_status(db: Session):
    db.commit()
