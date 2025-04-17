from pydantic_settings import SettingsConfigDict

from config.base import SettingsBase


class DBSettings(SettingsBase):
    model_config = SettingsConfigDict(env_prefix="DB_")

    HOST: str
    PORT: str
    USER: str
    PASS: str
    NAME: str

    @property
    def database_url_asyncpg(self):
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}".format(
            user=self.USER,
            password=self.PASS,
            host=self.HOST,
            port=self.PORT,
            name=self.NAME,
        )


db_settings = DBSettings.load()
