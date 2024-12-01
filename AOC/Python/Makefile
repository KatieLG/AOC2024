lint:
	uv run ruff format
	uv run ruff check --fix

test:
	uv run pytest

check: lint test

today:
	uv run python -m helpers fetch

today-p2:
	uv run python -m helpers fetch --part 2
