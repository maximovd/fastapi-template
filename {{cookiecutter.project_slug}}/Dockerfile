FROM python:3.10

RUN apt-get update && apt-get -y install gcc
RUN pip3 install --upgrade pip

WORKDIR /code

COPY . code/

{% if cookiecutter.package_manager == 'poetry' %}
RUN pip3 install poetry
{% else %}
RUN pip3 install pipenv
{% endif %}

CMD ["/bin/sh", "code/entrypoint.sh"]
