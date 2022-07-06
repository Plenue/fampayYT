from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Video(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    channel_name = Column(String, nullable=False)
    url = Column(String)
    description = Column(String, nullable=False)
    date_posted = Column(DateTime)
