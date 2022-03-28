import os
from pathlib import Path

def choice_package_manger():
    if "{{ cookiecutter.package_manager }}".lower() == "poetry":
        os.remove("Pipfile")
        os.remove("Pipfile.lock")
    else:
        os.remove("pyproject.toml")
        os.remove("poetry.lock")

def extract_env_variables():
    with open(".env.example", "r") as example_file, open(".env", "a") as target_file:
        for line in example_file:
            target_file.write(line)

def fix_endlines_for_sh_files():
    path: Path
    for path in Path(".").glob("**/*.sh"):
        lf_data = path.read_bytes().replace(b"\r\n", b"\n")
        path.write_bytes(lf_data)
    makefile = Path(".", "Makefile")
    lf_data = makefile.read_bytes().replace(b"\r\n", b"\n")
    makefile.write_bytes(lf_data)

if __name__ == "__main__":
    choice_package_manger()
    fix_endlines_for_sh_files()
    if os.path.isfile(".env.example"):
        extract_env_variables()
