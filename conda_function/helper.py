import subprocess
import threading
from contextlib import contextmanager
from pathlib import Path
from typing import Generator, List, Optional, Text, TypeVar, Union

from packaging.requirements import Requirement

from conda_function.config import console

T = TypeVar("T")


def subprocess_run(args: List[Text], cwd: Optional[Union[Text, Path]] = None):
    try:
        args_str = " ".join(args)
        console.print(f"Executing: [italic underline]{args_str}[/italic underline]")
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            cwd=cwd,
            text=True,
            bufsize=1,
        )
        stdout_thread = threading.Thread(target=print_output, args=(process.stdout,))
        stderr_thread = threading.Thread(target=print_output, args=(process.stderr,))
        stdout_thread.start()
        stderr_thread.start()
        process.wait()
        stdout_thread.join()
        stderr_thread.join()
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


@contextmanager
def dummy_ctx(value: T) -> Generator[T, None, None]:
    yield value


def print_output(stream):
    for line in iter(stream.readline, ""):
        print(line, end="")
