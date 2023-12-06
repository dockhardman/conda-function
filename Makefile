install:
	poetry install --no-root

upgrade-deps:
	poetry update
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	poetry export -f requirements.txt --with dev -E all --output requirements-all.txt --without-hashes

format-code:
	isort . && black .

test-make:
	echo "make test"