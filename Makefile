.PHONY: clean clean-test clean-pyc clean-build tests lint bdd

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

tests: ## test and lint
	python3 -m pytest tests/ -v -W ignore::DeprecationWarning --cov=tests --cov=py_file_organizer --cov-report term-missing:skip-covered

lint: tests
	@echo "Linting..."
	@flake8 .
	@echo "\033[32mTudo certo!"

bdd: ## run bdd tests
	python3 -m pytest bdd/ -v -W ignore::DeprecationWarning --cov=bdd --cov=py_file_organizer --cov-report term-missing:skip-covered --cov-config=.bdd-coveragerc
