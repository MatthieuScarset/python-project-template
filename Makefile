.PHONY: dev serve test lint format clean

dev:
	uv run uvicorn mypackage.main:app --reload

serve:
	uv run uvicorn mypackage.main:app --host 0.0.0.0 --port 8000

test:
	uv run pytest

lint:
	uv run ruff check --fix .

format:
	uv run ruff format .

check:
	uv run mypy .

clean:
	rm -rf __pycache__ .pytest_cache dist build *.egg-info
