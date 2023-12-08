import subprocess
from typing import List, Text


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
