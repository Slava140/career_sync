from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


env_path = Path(__file__).parent.parent.parent / '.env'


class SettingsBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_path if env_path.exists() else None,
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @classmethod
    def load(cls):
        return cls()
