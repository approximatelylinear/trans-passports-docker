include .env

.DEFAULT_GOAL=build

local_build:
	@echo "Building the local containers..."
	docker-compose -f compose/local.yml build

local_up:
	@echo "Composing the local containers..."
	docker-compose -f compose/local.yml up

prod_build:
	@echo "Building the prod containers..."
	docker-compose -f compose/prod.yml build

prod_up:
	@echo "Composing the prod containers..."
	docker-compose -f compose/prod.yml up

