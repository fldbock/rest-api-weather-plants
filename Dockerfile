FROM python:3.8.10-slim-buster

WORKDIR /weather-plants-docker

COPY ./app ./app
COPY ./public ./public
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV FLASK_APP="public.index"

RUN pipenv install

RUN flask db init &&\
    flask db migrate &&\
    flask db upgrade

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]