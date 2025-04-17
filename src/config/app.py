from pydantic_settings import SettingsConfigDict

from config.base import SettingsBase


class AppSettings(SettingsBase):
    model_config = SettingsConfigDict(env_prefix='APP_')

    HOST: str
    PORT: int


app_settings = AppSettings.load()
