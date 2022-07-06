import re
from sqlalchemy.orm import Session
from sqlalchemy import desc, and_, or_

from app.db.models.videos import Video

# Add Pagination
def search_videos(query: str, db: Session):
    try:
        if query == "":
            video_list_db = db.query(Video).order_by(desc(Video.date_posted))
        else:
            pat = re.compile(r"[^a-zA-Z 0-9]+")
            processed_query = re.sub(pat, "", query)
            token = processed_query.split()

            video_list_db = []

            clauses = [Video.title.like(elem) for elem in token]
            query = (
                db.query(Video).filter(or_(*clauses)).order_by(desc(Video.date_posted))
            )
            video_list_db = query.all()

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

    except Exception as e:
        print("app.utils.get_videos: ORM Call")
        print(e)
