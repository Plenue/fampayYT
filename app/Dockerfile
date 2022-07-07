#
FROM python:3.9-buster

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./ /code/app

#
COPY ./wait /code/wait

# 
COPY ./start.sh /code/start.sh

#
RUN chmod +x /code/wait

#
RUN chmod +x /code/start.sh

#
CMD /code/wait && /code/start.sh