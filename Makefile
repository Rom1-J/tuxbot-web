PYTHON_PATH := .venv/bin/python
TESTS := tuxbot_web/pages/tests/ tuxbot_web/users/tests/

lint:
	$(PYTHON_PATH) -m pylint tuxbot_web --load-plugins=pylint_django --django-settings-module=config.settings.local $(addprefix -d duplicate-code , $(TESTS))

black:
	$(PYTHON_PATH) -m black tuxbot_web --line-length=79

type:
	$(PYTHON_PATH) -m mypy tuxbot_web

test:
	$(PYTHON_PATH) -m pytest
