FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get -y install gcc
RUN pip3 install --upgrade pip

{% if cookiecutter.package_manager == 'poetry' %}
COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock
RUN pip3 install poetry
{% else %}
COPY ./Pipfile /code/Pipfile
COPY ./Pipfile.lock /code/Pipfile.lock
RUN pip3 install pipenv
RUN pipenv install --system
{% endif %}

COPY . /code

CMD ["/bin/bash", "entrypoint.sh"]
