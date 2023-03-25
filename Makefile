NAME ?= opensips
OPENSIPS_VERSION ?= 3.3
OPENSIPS_BUILD ?= releases
OPENSIPS_DOCKER_TAG ?= latest
OPENSIPS_CLI ?= true
OPENSIPS_EXTRA_MODULES ?=

all: build start

.PHONY: build start
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
	docker exec -it $(NAME) bin/bash

host:
	docker run -d --net=host --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG)

start:
	docker run -d -p 8000:8000/tcp -p 5060:5060/udp --name $(NAME) opensips/opensips:$(OPENSIPS_DOCKER_TAG)
	docker exec -it $(NAME) bin/bash

kill:
	docker kill $(NAME)
	docker rm $(NAME)