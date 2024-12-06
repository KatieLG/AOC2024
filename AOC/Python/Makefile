day := $(shell date +%d )

lint:
	uv run ruff format
	uv run ruff check --fix

test:
	uv run pytest

check: lint test

today:
	uv run python -m helpers fetch --day $(day)

today-p2:
	uv run python -m helpers fetch --part 2 --day $(day)

run:
	uv run python -m solutions.day_$(day)

profile:
	uv run python -m cProfile -s tottime solutions/day_$(day).py
