from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_name: str
    db_pass: str


    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def database_url(self) -> str:
        return f"mysql+aiomysql://root:{self.db_pass}@db:3306/{self.db_name}"

@lru_cache
def get_settings():
    return Settings()
