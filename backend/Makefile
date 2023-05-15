NAME ?= backend


build:
	docker image build -t dockerfile_test .
 

start:
	docker run -d -p 80:8888 --name $(NAME) dockerfile_test

test:
	docker run -it -p 80:8888 --name $(NAME) dockerfile_test


kill:
	docker kill $(NAME);docker rm $(NAME)