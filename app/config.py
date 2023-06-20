from functools import lru_cache
from typing import Optional, Dict, Any
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    cors_origins: str
    postgres_host: str
    postgres_port: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    sqlalchemy_database_uri: Optional[PostgresDsn] = None
    sqlalchemy_database_connect_timezone: str
    api_key: str

    @validator("sqlalchemy_database_uri")
    def assemble_db_connection(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            host=values.get("postgres_host"),
            port=values.get("postgres_port"),
            user=values.get("postgres_user"),
            password=values.get("postgres_password"),
            path=f"/{values.get('postgres_db') or ''}",
        )

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
