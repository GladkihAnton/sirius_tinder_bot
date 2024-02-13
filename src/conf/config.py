from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TINDER_BACKEND_HOST: str = 'http://localhost:8000'
    #
    # JWT_SECRET_SALT: str
    # KAFKA_BOOTSTRAP_SERVERS: List[str]
    # KAFKA_TOPIC: str
    #
    # REDIS_HOST: str
    # REDIS_PORT: int
    # REDIS_PASSWORD: str
    # REDIS_SIRIUS_CACHE_PREFIX: str = 'sirius'
    #

settings = Settings()
