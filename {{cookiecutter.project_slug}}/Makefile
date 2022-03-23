

.PHONY: all

SHELL=/bin/bash -e

.DEFAULT_GOAL := help


help:


docker_req_install:
	{% if cookiecutter.package_manager == 'pipenv' %}
		pipenv install --system
	{% else %}
		poetry config virtualenvs.create false
		poetry install --no-root
	{% endif %}
migrate:
	alembic upgrade head


run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000
