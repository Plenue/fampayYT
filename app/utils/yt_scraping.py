import requests
from sqlalchemy.orm import Session

from app.core.config import settings
from app.utils.helper.add_videos import add_new_videos
from app.utils.helper.last_published import get_latest_date


def yt_scraping(db: Session):
    to_fetch = True
    while to_fetch:
        for token in settings.YT_API_KEY:
            url = (
                "https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=date&key="
                + token
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
                    videoEntry["thumbnail_url"] = video["snippet"]["thumbnails"][
                        "high"
                    ]["url"]
                    videoEntry["description"] = video["snippet"]["description"]
                    videoEntry["date_posted"] = video["snippet"]["publishedAt"]

                    videoList.append(add_new_videos(videoEntry, db))

                to_fetch = False
                print(str(cnt) + " Records Pushed")
                break

            else:
                error = response.json()
                if (
                    response.status_code == 403
                    and error["error"]["message"]
                    == 'The request cannot be completed because you have exceeded your <a href="/youtube/v3/getting-started#quota">quota</a>.'
                ):
                    print("Changing API Key")
                else:
                    print(
                        "app.utils.yt_scraping: API Error; Status Code:"
                        + str(response.status_code)
                    )
                    print(error)
    if to_fetch:
        print("app.utils.yt_scraping: ALL Token Expired. Can not fetch")

