import json
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.db.models.videos import Video

# Add Query, Pagination
def search_videos(db: Session, query=""):
    video_list_db = db.query(Video).order_by(desc(Video.date_posted))
    video_list = []

    for video_db in video_list_db:
        video = {}
        video["title"] = video_db.title
        video["channel_name"] = video_db.channel_name
        video["url"] = video_db.url
        video["description"] = video_db.description
        video["date_posted"] = video_db.date_posted

        video_list.append(video)

    response = {}
    response["status"] = "Success"
    response["data"] = video_list

    return response

