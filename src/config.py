from pathlib import Path
from os import path

from pydantic_settings import BaseSettings, SettingsConfigDict


env_path = Path(__file__).parent.parent / '.env'


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    JWT_SECRET: str
    JWT_LIFETIME: int

    src_path: Path = Path(__file__).parent

    @property
    def database_url_asyncpg(self):
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}".format(
            user=self.DB_USER,
            password=self.DB_PASS,
            host=self.DB_HOST,
            port=self.DB_PORT,
            name=self.DB_NAME,
        )

    if path.exists(env_path):
        model_config = SettingsConfigDict(env_file=env_path)


settings = Settings()