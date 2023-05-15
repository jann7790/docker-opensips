NAME ?= opensips
OPENSIPS_VERSION ?= 3.3
OPENSIPS_BUILD ?= releases
OPENSIPS_DOCKER_TAG ?= latest
OPENSIPS_CLI ?= true
OPENSIPS_EXTRA_MODULES ?= opensips-mysql-module

HOST_IP=$(shell ip route get 8.8.8.8 | head -n +1 | tr -s " " | cut -d " " -f 7)
# HOST_IP= 127.0.0.1



all:
	
	make build
	make start
	make init_database
	make attach



build:
	docker build \
		--build-arg=HOST_IP=$(HOST_IP) \
		--build-arg=OPENSIPS_BUILD=$(OPENSIPS_BUILD) \
		--build-arg=OPENSIPS_VERSION=$(OPENSIPS_VERSION) \
		--build-arg=OPENSIPS_CLI=${OPENSIPS_CLI} \
		--build-arg=OPENSIPS_EXTRA_MODULES="${OPENSIPS_EXTRA_MODULES}" \
		--tag="opensips/opensips:$(OPENSIPS_DOCKER_TAG)" \
		.

# docker run -d --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG)
 
init_database:
	docker exec -it $(NAME)  service mariadb start

	docker exec -i $(NAME)  mysql -t <  createDBUser.sql

	echo NO PASSWORD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!, just press enter directly nextline
	docker exec -it $(NAME)  opensips-cli -x database create


	echo YOUR IP!!!!!!!!!!!!!!!!!!!!!!:$(HOST_IP)
	docker exec -it $(NAME)  opensips-cli -x user add 1000 123456;


attach:
	docker exec -it $(NAME)  bin/bash

#only supported on linux hosts
host:
	docker run -d --network host --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG)


# -it
test:
	docker run -it -p 8000:8000/tcp -p 5060:5060/udp --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG)

# -d
start:
	docker run -d -p 3306:3306/tcp -p 5060:5060/udp --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG)

kill:
	docker kill $(NAME);docker rm $(NAME)