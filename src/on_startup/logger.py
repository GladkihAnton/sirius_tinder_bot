import logging.config

from src.logger import LOGGING_CONFIG, logger

from conf.config import settings


def setup_logger() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)

    if settings.LOG_LEVEL == 'debug':
        logger.setLevel(logging.DEBUG)
