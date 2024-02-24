format:
	ruff format .
	ruff format src
	isort src
	isort .
	
check:
	ruff check --fix .
	ruff check --fix src

build-docker:
	docker build -t kitty-list .

run-docker:
	docker run -p 8080:8080 kitty-list