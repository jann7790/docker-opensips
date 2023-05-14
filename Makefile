# NAME ?= opensips
NAME ?= fucktest
OPENSIPS_VERSION ?= 3.3
OPENSIPS_BUILD ?= releases
OPENSIPS_DOCKER_TAG ?= latest
OPENSIPS_CLI ?= true
OPENSIPS_EXTRA_MODULES ?=
HOST_IP=$(ip route get 8.8.8.8 | head -n +1 | tr -s " " | cut -d " " -f 7)
HOST_IP=$(shell ip route get 8.8.8.8 | head -n +1 | tr -s " " | cut -d " " -f 7)
HOST_IP= 127.0.0.1



all: build start



build:
	docker build \
		--build-arg=OPENSIPS_BUILD=$(OPENSIPS_BUILD) \
		--build-arg=OPENSIPS_VERSION=$(OPENSIPS_VERSION) \
		--build-arg=OPENSIPS_CLI=${OPENSIPS_CLI} \
		--build-arg=OPENSIPS_EXTRA_MODULES="${OPENSIPS_EXTRA_MODULES}" \
		--tag="opensips/opensips:$(OPENSIPS_DOCKER_TAG)" \
		.

# docker run -d --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG)
 
attach:
	docker exec -it $(NAME) "${HOST_IP}" bin/bash

#only supported on linux hosts
host:
	docker run -d --network host --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG)


test:
	docker run -d --ip=10.0.0.1 -p 8000:8000/tcp -p 5060:5060/udp --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG)
	docker exec -it $(NAME) bin/bash

start:
	# docker run -d -p 8000:8000/tcp -p 5060:5060/udp --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG) $(HOST_IP)
	# detach
	
	docker run -it -p 8000:8000/tcp -p 5060:5060/udp --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG) $(HOST_IP)
	docker exec -it $(NAME) "${HOST_IP}" bin/bash

kill:
	docker kill $(NAME);docker rm $(NAME)