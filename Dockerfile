FROM python:3.12-slim-bookworm

WORKDIR /weather-plants-docker

COPY ./app ./app
COPY ./public ./public
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

# Install pipvenv
RUN pip install pipenv
RUN pipenv install 

ENV FLASK_APP="public.index"

RUN flask db init &&\
    flask db migrate &&\
    flask db upgrade

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]