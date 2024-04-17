# rest-api-weather-plants
## Task Description
Create a REST API in Python to manage plants and query weather conditions for each plant:

* A plant has a name and location (geo coordinates)
* You need to be able to create, remove, edit and list plants.
* You need to be able to query the weather conditions (temperature and relative humidity) at a certain point in time for a specific plant (eg from ), but only on demand, there is no need to store them
* Choose your backend storage technology of choice. Motivate your choice.
* Add unit tests
* Package your application as a docker image (ie provide a dockerfile, not the image itself)
* Create a helm chart to deploy you application on a kubernetes cluster

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

Note: These instructions are written for ubuntu 20.04. 

For my local environment, I used a virtual environment called venv for dependency isolation. 

    python3 venv .venv
    source .venv/bin/activate


To install the python3 libraries use:

    pip3 install -r requirements.txt


To initialize the database:

    flask db init

    flask db migrate
    flask db upgrade


The last two commands need to be ran every time you make changes to the sql alchemy database scheme.


For executing the unit tests run:

    pytest

## Building The Docker Image (optional)

Run the following commands to create the docker image, and run it in a docker container. This is optional because in the next step we create the kubernetes cluster which gets the dockerimage from dockerhub.

    docker build --tag weather-plants-docker .

    docker run -d -p 5000:5000 weather-plants-docker

## Deploy to Kubernetes using Helm

Make sure minikube and kubectl are installed on your machine. Now you can start a minikube cluster where you can install your helm file.

    minikube start
    helm install -f weather-plants-helm/values.yaml weather-plant-helm ./ weather-plants-helm/

The output of your last command will give you new commands you should run to forward the port of your local machine to the minikube cluster.

## Querying The API Examples

Read list of plants:

    curl http://localhost:8080/plants

Create a new plant:

    curl -X POST -d "name=Plant1&lat=15.15&long=16.16" http://localhost:8080/plants

Update the plant with id 1:

    curl -X PUT -d "name=Plant2&lat=50.00&long=60.00" http://localhost:8080/plants/1

Remove plant with id 1:

    curl -X DELETE http://localhost:8080/plants/1

Get the temperature and relative humidity for the plant with id 1 at datetime 2024-04-15T02:00:

    curl http://localhost:8080/plants/1/weather?datetime=2024-04-15T02:00


