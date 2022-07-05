from sqlalchemy.orm import Session

from app.schemas.videos import VideoCreate
from app.db.models.videos import Video


def dbStatus(db: Session):
    db.commit()
