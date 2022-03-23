import os

def choice_package_manger():
    if "{{ cookiecutter.package_manager }}".lower() == "poetry":
        os.remove("Pipfile")
    else:
        os.remove("pyproject.toml")

def extract_env_variables():
    with open(".env.example", "r") as example_file, open(".env", "a") as target_file:
        for line in example_file:
            target_file.write(line)
 

if __name__ == "__main__":
    choice_package_manger()
    if os.path.isfile(".env.example"):
        extract_env_variables()

