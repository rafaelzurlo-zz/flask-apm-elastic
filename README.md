# POC flask with APM Elastic

## Dependencies

In order to build and run the application you need to have Docker installed and running in your machine: [Install docker](https://docs.docker.com/install/)

## Setup:

## Application setup
#### Create the containers web / elasticsearch / apm
`$ docker-compose build`

#### Set the container up web
`$ docker-compose up web`

#### The application will start at `localhost:5000` \o/
