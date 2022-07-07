# Fampay's Youtuber 🚀

---

## Description

A simple service to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Getting Started

### Setting up the Service

Please note that this Backend Service requires [Docker](https://www.docker.com).

1. Clone this repo (see [GitHub help](https://help.github.com/articles/fork-a-repo/) for details): `git clone https://github.com/Plenue/fampayYT`
1. Go to your cloned copy: `cd ./fampayYT/app`
1. Edit .env file and Add API KEYS values in `YT_API_KEY` Key for [YouTube Data API](https://developers.google.com/youtube/v3/getting-started).
1. (Optional) Change YouTube Search Keyword by updating `YT_SEARCH_QUERY` Key.

### Executing Service

**NOTE: Before you run the service, don't forget to Add [YouTube Data](https://developers.google.com/youtube/v3/getting-started) API Keys !**

In the cloned repo folder, type:

```
docker-compose up --build
```

Service will start running on `localhost:8000/`.

You should be able to access Swagger of the service at `localhost:8000/docs#/`.

---

-- Shashi Fagna
