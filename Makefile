format:
	ruff format .
	ruff format src
	isort src
	isort .
	
check:
	ruff check --fix .
	ruff check --fix src