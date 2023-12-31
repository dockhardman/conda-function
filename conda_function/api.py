import tempfile
from pathlib import Path
from typing import List, Optional, Text, Union

from conda_function.config import default_settings
from conda_function.helper import dummy_ctx, subprocess_run
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

    def run_in_conda_env(
        self,
        env_name: Text,
        command: List[Text],
        cwd: Optional[Union[Text, Path]] = None,
    ) -> None:
        if not self.is_conda_env_exist(env_name):
            raise Exception(f"Conda environment {env_name} does not exist")
        with dummy_ctx(cwd) if cwd else tempfile.TemporaryDirectory() as tmp_dir:
            out = subprocess_run(
                ["conda", "run", "--no-capture-output", "-n", env_name] + command,
                cwd=tmp_dir,
            )
            return out

    def run_script_in_conda_env(
        self,
        env_name: Text,
        script_path: Text,
        cwd: Optional[Union[Text, Path]] = None,
    ) -> None:
        if not self.is_conda_env_exist(env_name):
            raise Exception(f"Conda environment {env_name} does not exist")
        with dummy_ctx(cwd) if cwd else tempfile.TemporaryDirectory() as tmp_dir:
            out = self.run_in_conda_env(
                env_name=env_name,
                command=["python", "-u", script_path],
                cwd=tmp_dir,
            )
            return out


default_conda_api = CondaAPI()
