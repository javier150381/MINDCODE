from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./dev.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    STRIPE_SECRET: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""
    META_WA_VERIFY_TOKEN: str = ""
    META_WA_TOKEN: str = ""
    DEEPSEEK_API_BASE: str = ""
    DEEPSEEK_API_KEY: str = ""
    ENV: str = "development"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
