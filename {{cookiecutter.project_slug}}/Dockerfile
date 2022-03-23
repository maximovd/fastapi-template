FROM python:3.10

WORKDIR /code

COPY . code/

{% if cookiecutter.package_manager == 'poetry' %}
RUN pip3 install poetry
{% else %}
RUN pip3 install pipenv
{% endif %}

CMD ["/bin/sh", "code/entrypoint.sh"]
