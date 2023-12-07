import os
from typing import Text


class Settings:
    CONDA_DEFAULT_ENV: Text
    CONDA_EXE: Text
    CONDA_PREFIX: Text
    CONDA_PREFIX_1: Text
    CONDA_PROMPT_MODIFIER: Text
    CONDA_PYTHON_EXE: Text
    CONDA_SHLVL: Text

    def __init__(self, *args, **kwargs):
        self.CONDA_DEFAULT_ENV = os.environ.get("CONDA_DEFAULT_ENV")
        self.CONDA_EXE = os.environ.get("CONDA_EXE")
        self.CONDA_PREFIX = os.environ.get("CONDA_PREFIX")
        self.CONDA_PREFIX_1 = os.environ.get("CONDA_PREFIX_1")
        self.CONDA_PROMPT_MODIFIER = os.environ.get("CONDA_PROMPT_MODIFIER")
        self.CONDA_PYTHON_EXE = os.environ.get("CONDA_PYTHON_EXE")
        self.CONDA_SHLVL = os.environ.get("CONDA_SHLVL")


default_settings = Settings()
