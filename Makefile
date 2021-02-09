DOCKER_LOCAL := docker-compose -f local.yml
DOCKER_DJANGO := $(DOCKER_LOCAL) run --rm django
VIRTUAL_ENV := .venv
PYTHON_PATH := $(VIRTUAL_ENV)/bin/python
TESTS := tuxbot_web/pages/tests/ tuxbot_web/users/tests/

.PHONY: lint
lint:
	$(PYTHON_PATH) -m pylint tuxbot_web --load-plugins=pylint_django --django-settings-module=config.settings.local $(addprefix -d duplicate-code , $(TESTS))

.PHONY: black
black:
	$(PYTHON_PATH) -m black tuxbot_web --line-length=79

.PHONY: type
type:
	$(PYTHON_PATH) -m mypy tuxbot_web

.PHONY: test
test:
	$(DOCKER_DJANGO) pytest

.PHONY: coverag
coverage:
	$(DOCKER_DJANGO) coverage run -m pytest
	$(DOCKER_DJANGO) coverage report

.PHONY: rebuild
rebuild:
	$(DOCKER_LOCAL) build

.PHONY: migrate
migrate:
	$(DOCKER_DJANGO) python manage.py migrate
