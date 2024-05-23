install:
	poetry install

format:
	poetry run black *.py

lint:
	poetry run pylint --disable=R,C app.py

test:
	poetry run python test_app.py
