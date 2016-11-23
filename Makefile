include .env

.DEFAULT_GOAL=build

build_api:
	@echo "Building api..."
	docker-compose -f compose/local.yml build

build_frontend:
	@echo "Building frontend..."
	docker-compose build trans_passports_frontend

local_build:
	@echo "Building the local containers..."
	docker-compose -f compose/local.yml build

local_up:
	@echo "Composing the local containers..."
	docker-compose -f compose/local.yml up
