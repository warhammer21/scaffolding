install:
	poetry install

format:
	poetry run black *.py

lint:
	poetry run pylint --disable=W0718 --disable=R,C app.py

test:
	poetry run python test_app.py
