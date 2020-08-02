.PHONY: build
build:
	@echo "Building docker images"
	docker image rm -f my_consumer
	docker image rm -f my_producer
	docker build -t my_producer -f ./producer/DockerFile .
	docker build -t my_consumer -f ./consumer/DockerFile .

.PHONY: start
start:
	docker-compose down
	docker-compose up -d
