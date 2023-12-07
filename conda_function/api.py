from conda_function.config import default_settings
from typing import Text
from pathlib import Path


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


default_conda_api = CondaAPI()
