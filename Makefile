.PHONY: init run clean

init:
	uv sync
	uv run pre-commit install

run:
	uv run jupyter lab

clean:
	rm -rf .venv __pycache__ .ruff_cache .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
