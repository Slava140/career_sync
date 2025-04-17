from pydantic_settings import SettingsConfigDict

from config.base import SettingsBase


class EmailSettings(SettingsBase):
    model_config = SettingsConfigDict(env_prefix='EMAIL_')

    HOST: str
    PORT: int
    USER: str
    PASS: str


email_settings = EmailSettings.load()
