test:
	@echo "🚀 Running tests..."
	@python3 -m pytest -n 3

test_single:
	@echo "🚀 Running test single..."
	@python3 -m pytest --tb=auto -k "test_create_pg_inline_success" -s 	

	