.PHONY: all

SHELL=/bin/bash -e

.DEFAULT_GOAL := help


help:
	echo 'Change this help message'

migrate:
	alembic upgrade head

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000
