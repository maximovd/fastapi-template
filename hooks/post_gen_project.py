import os

def choice_package_manger():
    if "{{ cookiecutter.package_manager }}".lower() == "poetry":
        os.remove("Pipfile")
    else:
        os.remove("pyproject.toml")


if __name__ == "__main__":
    choice_package_manger()