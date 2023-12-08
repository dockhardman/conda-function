from pathlib import Path
from typing import List, Text

from conda_function.config import default_settings
from conda_function.helper import subprocess_run
from conda_function.schemas import CondaEnv


class CondaAPI:
    def is_conda(self):
        return default_settings.CONDA_DEFAULT_ENV is not None

    def is_conda_env_exist(self, env_name: Text) -> bool:
        if default_settings.CONDA_PREFIX_1 is None:
            raise Exception("Not in conda environment")
        return (
            Path(default_settings.CONDA_PREFIX_1)
            .joinpath("envs")
            .joinpath(env_name)
            .is_dir()
        )

    def list_envs(self) -> List[CondaEnv]:
        output = subprocess_run(["conda", "env", "list"])
        lines = output.splitlines()
        conda_envs: List[CondaEnv] = []
        for line in lines:
            if line and not line.startswith("#"):
                parts = line.split()
                conda_envs.append(
                    CondaEnv(
                        name=parts[0],
                        active=len(parts) == 3,
                        conda_prefix=parts[-1],
                    )
                )
        return conda_envs


default_conda_api = CondaAPI()
