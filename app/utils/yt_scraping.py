import requests
from sqlalchemy.orm import Session

from app.core.config import settings
from app.utils.add_videos import add_new_videos
from app.utils.last_published import get_latest_date


def yt_scraping(db: Session):
    url = (
        "https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=date&key="
        + settings.YT_API_KEY
        + "&type=video"
        + "&q="
        + settings.YT_SEARCH_QUERY
    )

    date_time = get_latest_date(db)
    if date_time != None:
        url = (
            url
            + "&publishedAfter="
            + date_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-4]
            + "Z"
        )

    payload = {}
    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        cnt = 0
        videoList = []
        result = response.json()

        for video in result["items"]:
            cnt = cnt + 1
            videoEntry = {}
            videoEntry["title"] = video["snippet"]["title"]
            videoEntry["channel_name"] = video["snippet"]["channelTitle"]
            videoEntry["url"] = video["snippet"]["thumbnails"]["high"]["url"]
            videoEntry["description"] = video["snippet"]["description"]
            videoEntry["date_posted"] = video["snippet"]["publishedAt"]

            videoList.append(add_new_videos(videoEntry, db))
        print(str(cnt) + " Records Pushed")
    else:
        error = response.json()
        if response.status_code == 403:
            print("Change API Key as " + error["error"]["message"])
        else:
            print("Error while fetching" + str(response.status_code))
