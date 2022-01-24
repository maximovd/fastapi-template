import os
import subprocess

def delete_manager():
    command = 'cookiecutter.package_manager'
    if subprocess.Popen(command, stdout=subprocess.PIPE) == "poetry":
        os.remove("Pipfile")
    else:
        os.remove("pyproject.toml")
