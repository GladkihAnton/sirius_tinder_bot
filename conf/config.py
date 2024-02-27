from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TINDER_BACKEND_HOST: str = 'http://web:8000'

    BOT_TOKEN: str
    WEBHOOK_URL: str = ''

    REDIS_HOST: str = 'redis'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str
    REDIS_DB: int = 0


settings = Settings()
