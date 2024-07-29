FROM python:3.12-slim-bookworm

WORKDIR /weather-plants-docker

COPY ./app ./app
COPY ./public ./public
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

# Install pipvenv
RUN pip install pipenv
RUN pipenv install --system

ENV FLASK_APP="public.index" \
    APP_CONFIG_FILE=.env

ENTRYPOINT ["entrypoint.sh"]