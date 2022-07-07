import re
import math
from sqlalchemy.orm import Session
from sqlalchemy import desc, and_, or_

from app.db.models.videos import Video


def search_videos(query: str, per_page_count: int, page_no: int, db: Session):
    try:
        if query == "":

            row_count = db.query(Video).order_by(desc(Video.date_posted)).count()
            if row_count < per_page_count * (page_no - 1):
                allowed_page_no = math.ceil(row_count / per_page_count)
                response = {}
                response["status"] = "Failed"
                response["message"] = (
                    "Page Number Overflow - Maximum allowed page number for given per_page_count is "
                    + str(allowed_page_no)
                )

                return response

            video_list_db = (
                db.query(Video)
                .order_by(desc(Video.date_posted))
                .offset((page_no - 1) * per_page_count)
                .limit(per_page_count)
                .all()
            )

        else:
            pat = re.compile(r"[^a-zA-Z 0-9]+")
            processed_query = re.sub(pat, "", query)
            token = [("% " + t + " %") for t in processed_query.split()]

            video_list_db = []
            clauses_title = [Video.title.like(elem) for elem in token]
            clauses_description = [Video.description.like(elem) for elem in token]
            clauses = clauses_title + clauses_description

            row_count = (
                db.query(Video)
                .filter(or_(*clauses))
                .order_by(desc(Video.date_posted))
                .count()
            )
            if row_count < per_page_count * (page_no - 1):
                allowed_page_no = math.ceil(row_count / per_page_count)
                response = {}
                response["status"] = "Failed"
                response["message"] = (
                    "Page Number Overflow - Maximum allowed page number for given per_page_count is "
                    + str(allowed_page_no)
                )

                return response

            query = (
                db.query(Video)
                .filter(or_(*clauses))
                .order_by(desc(Video.date_posted))
                .offset((page_no - 1) * per_page_count)
                .limit(per_page_count)
            )
            video_list_db = query.all()

        video_list = []
        for video_db in video_list_db:
            video = {}
            video["title"] = video_db.title
            video["channel_name"] = video_db.channel_name
            video["thumbnail_url"] = video_db.thumbnail_url
            video["description"] = video_db.description
            video["date_posted"] = video_db.date_posted

            video_list.append(video)

        response = {}
        response["status"] = "Success"
        response["data"] = video_list

        return response

    except Exception as e:
        response = {}
        response["status"] = "Failed"
        response["message"] = (
            "app.utils.get_videos - ORM Call: "
            + str(e)
        )

        return response
