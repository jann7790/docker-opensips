NAME ?= backend
HOST_IP=$(shell ip route get 8.8.8.8 | head -n +1 | tr -s " " | cut -d " " -f 7)


build:
	docker image build -t dockerfile_test \
		--build-arg=HOST_IP=$(HOST_IP) \
		.

start:
	docker run -d -p 80:8888 --name $(NAME) dockerfile_test

test:
	docker run -it -p 80:8888 --name $(NAME) dockerfile_test


kill:
	docker kill $(NAME);docker rm $(NAME)