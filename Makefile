test:
	@echo "🚀 Running tests..."
	@python3 -m pytest -n 3

test_single:
	@echo "🚀 Running test single..."
	@python3 -m pytest -k "TestCreateQuotationExcel" -s

	

