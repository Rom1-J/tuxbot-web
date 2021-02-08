PYTHON_PATH := .venv/bin/python

lint:
	$(PYTHON_PATH) -m pylint --load-plugins=pylint_django --django-settings-module=config.settings.local tuxbot_web

black:
	$(PYTHON_PATH) -m black tuxbot_web --line-length=79

type:
	$(PYTHON_PATH) -m mypy tuxbot_web
