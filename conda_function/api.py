from conda_function.config import default_settings


class CondaAPI:
    def is_conda(self):
        return default_settings.CONDA_DEFAULT_ENV is not None


default_conda_api = CondaAPI()
