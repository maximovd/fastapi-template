#!/bin/bash

# shellcheck disable=SC1083
rm {{ "Pipfile" if cookiecutter.package_manager == "poetry" else "pyproject.toml" }}