#
FROM python:3.9-buster

# 
WORKDIR /code

#
# RUN apt-get update && apt-get install -y cron busybox

# 
COPY ./requirements.txt /code/requirements.txt

#
# COPY ./crontab /code/crontab

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./ /code/app

#
CMD ["uvicorn", "app.main:app", "--reload" ,"--host", "0.0.0.0", "--port", "8000"]