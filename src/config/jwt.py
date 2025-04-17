from datetime import timedelta

from pydantic_settings import SettingsConfigDict

from config.base import SettingsBase


class JWTSettings(SettingsBase):
    model_config = SettingsConfigDict(env_prefix='JWT_')

    SECRET: str
    ACCESS_TOKEN_LIFETIME: int

    @property
    def access_token_lifetime_timedelta(self):
        return timedelta(seconds=self.ACCESS_TOKEN_LIFETIME)


jwt_settings = JWTSettings.load()
