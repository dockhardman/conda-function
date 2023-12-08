import subprocess
from typing import List, Text

from packaging.requirements import Requirement


def subprocess_run(args: List[Text]):
    try:
        result = subprocess.run(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            encoding="utf-8",
        )
        return (
            result.stdout.decode("utf-8")
            if isinstance(result.stdout, bytes)
            else result.stdout
        )
    except subprocess.CalledProcessError as e:
        print(
            f"Error: {e.stderr.decode('utf-8') if isinstance(e.stderr, bytes) else e.stderr}"
        )
    except Exception as e:
        print(f"An error occurred: {e}")


def read_requirements(file_path: Text = "requirements.txt") -> List["Requirement"]:
    with open(file_path, "r") as file:
        requirements = file.readlines()
    return [Requirement(req) for req in requirements if req.strip()]


def install_requirements(requirements: List["Requirement"]) -> None:
    if not requirements:
        return
    subprocess_run(["pip", "install"] + [str(req) for req in requirements])


def install_requirements_from_file(file_path: Text = "requirements.txt") -> None:
    if not file_path:
        return
    subprocess_run(["pip", "install", "-r", file_path])
