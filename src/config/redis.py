from pydantic_settings import SettingsConfigDict

from config.base import SettingsBase


class RedisSettings(SettingsBase):
    model_config = SettingsConfigDict(env_prefix="REDIS_")

    HOST: str
    PORT: int
    USER: str
    PASS: str

    @property
    def arq_redis_settings(self):
        from arq.connections import RedisSettings
        return RedisSettings(
            username=self.USER,
            password=self.PASS,
            host=self.HOST,
            port=self.PORT,
        )


redis_settings = RedisSettings.load()
