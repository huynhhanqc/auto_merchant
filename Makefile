test:
	@echo "🚀 Running tests..."
	@python3 -m pytest -n auto

test_single:
	@echo "🚀 Running test single..."
	@python3 -m pytest -k "Script_CreateQuotation" -n auto

	

