# Rest API Weather Plants
## Task Description
Create a REST API in Python to manage plants and query weather conditions for each plant:

- [x] A plant has a name and location (geo coordinates)
- [x] You need to be able to create, remove, edit and list plants.
- [x] You need to be able to query the weather conditions (temperature and relative humidity) at a certain point in time for a specific plant (eg from ), but only on demand, there is no need to store them
- [x] Choose your backend storage technology of choice. Motivate your choice.
- [x] Add unit tests
- [x] Package your application as a docker image (ie provide a dockerfile, not the image itself)
- [x] Create a helm chart to deploy you application on a kubernetes cluster

After finishing this initial project I added new requirements to implement more devops tools and techniques:

- [ ] App should be deployed both locally and on the cloud (prod)
- [ ] Database must be persistent and handle production loads

## Tech Stack
We use:
* Python3.8
* Flask3.0.3
* SQLalchemy
* SQLite
* Docker
* Kubernetes
* Helm

## Local Environment Setup (necessary to run the unit tests)

Note: These instructions are written for ubuntu 24.04. 

For my local environment, I use pyenv, pipenv and direnv for dependency isolation. This allows me to seperate the python version, installed packages and environment variables set between all my repositories. I recommend installing them and then running the following commands in the root of this repo.

    pipenv install --dev
    direnv allow


To initialize the database:

    flask db init

    flask db migrate
    flask db upgrade


The last two commands need to be ran every time you make changes to the sql alchemy database scheme.


For executing the unit tests run:

    pytest

## Building The Docker Image (optional)

Run the following commands to create the docker image.

    docker build --tag weather-plants-docker .