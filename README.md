# Advertising Test project

## Description 

Backend application written using FastAPI framework. 

Main features:
* Oauth authorization
* Managing advertisements: create, view, delete

Technological Stack:
* Python 3.10
* FastAPI
* SQLAlchemy
* Postgres using Docker

## Requirements

* python 3.10
* pip
* Installed libraries: <code>pip install -r requirements.txt</code>

## How to run application

* Setup all requirements described in the section above
* Start Postgres
* Initialize *.env* file with settings presented in *.env.example* 
* Inside *app* directory run <code>uvicorn main:app --reload --env-file ../.env </code>

## How to run tests

* In root directory run <code>pytest tests/</code>

## Future plans

* Tests
* Containerization using Docker
* Frontend
* NGINX