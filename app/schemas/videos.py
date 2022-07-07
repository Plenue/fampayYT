from typing import Optional
from pydantic import BaseModel


class VideoCreate(BaseModel):
    title: str
    channel_name: str
    thumbnail_url: str
    description: str
    date_posted: str
