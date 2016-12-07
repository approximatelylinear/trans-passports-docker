
# Trans-Passports Docker Project

This project represents a Docker deployment of Trans-Passports.


### Build/Deploy Status:

Master Branch: _Not configured_

Master Branch Code Coverage: _Not configured_

Deployment Status: _Not configured_


This project structures a python-based app.


## Docker

This project consists of the following docker containers:

* trans_passports_api - Rails API
* trans_passports_frontend - React-driven frontend (_in progress_)
* trans_passports_db - Postgres database
* trans_passports_redis - Redis cache
* nginx - NGINX server managed by supervisor (_in progress_)
* sumo - log aggregation client - customized per app (_in progress_)

## Building

For local building and testing, run the following command:

`make local_build`

For production building, run the following command:

`make prod_build`


## Running Containers

For local running, try the following:

`make local_up`

For production running, try the following:

`make prod_up`

If you're having trouble getting changes to be recognized, the following will build the images (forceably, even if the daemon doesn't think there have been updates) and will start containers.

`docker-compose -f compose/my_compose_file.yml -p trans_passports up --force-recreate -d`


### Running Tests

!!!TBD!!!

To run the test on this project you'd run the following command

`docker-compose -f compose/local.yml -p trans_passports run trans_passports_main bash ./opt/test_trans_passports_app.sh`

The test_trans_passports_app.sh file is the standard, regardless of the command needed to execute the commands.  All tech specific calls for tests should be executed from within that file.

## CI Integration

!!!TBD!!!

Inside the project - in the `compose` folder - you will see a file `ci.yml`. This file is what produces the build artifacts that are published to a docker registry.

## Deployment Templates

!!!TBD!!!

Also inside the project - in the `compose` folder - you will see target environment specific compose files, like `qa_template.yml` and `production_template.yml`.  These files are used as the jinja templates for the deployment pipeline.  They are responsible for receiving variables - like `imageTag` - that are supplied to them during the deployment process.  They are also responsible for setting all environment specific variables.
