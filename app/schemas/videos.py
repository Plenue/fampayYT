from typing import Optional
from pydantic import BaseModel


class VideoCreate(BaseModel):
    title: str
    channel_name: str
    url: str
    description: str
    date_posted: str
