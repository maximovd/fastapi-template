# {{cookiecutter.project_name}}

## Backend Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.
* [Pipenv](https://pipenv.pypa.io/en/latest/) another Python package manager.
> You have to choose which manager you will use for your project

## Local development

* Start with Docker Compose:
```shell
docker-compose up -d
```

* To check logs run:
```shell
docker-compose logs web
```

* To test run:
```shell
pytest
```
