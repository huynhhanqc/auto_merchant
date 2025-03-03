PYTHON = python3
PIP = pip
PYTEST = pytest
PROJECT_DIR = .
TEST_DIR = tests
SCREENSHOTS_DIR = screenshots

clean:
	@echo "Xóa file tạm, screenshots, và report..."
	@rm -rf $(SCREENSHOTS_DIR)/*
	@rm -rf $(LOG_DIR)/*
	@rm -f report.html report_single.html report_debug.html

test:
	@echo "🚀 Running tests..."
	@python3 -m pytest -n 3

test_single:
	@echo "🚀 Running test single..."
	@python3 -m pytest --tb=auto -k "tests" -s -n auto

test_debug:
	@echo "🚀 Running test debug..."
	@python3 -m pytest --log-cli-level=DEBUG --tb=auto -k "test_create_pg_inline_success" -s


Testiest:
	@echo $(LOG_DIR)/*