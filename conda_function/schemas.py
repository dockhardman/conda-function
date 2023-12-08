from typing import Text

from typing_extensions import TypedDict


class CondaEnv(TypedDict):
    name: Text
    active: bool
    conda_prefix: Text
