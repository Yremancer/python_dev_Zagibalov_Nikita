import logging

from core.config import get_settings


def setup_logger():
    settings = get_settings()
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level.upper())

    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
    )
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    logging.getLogger("aiomysql").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


def get_logger(name: str):
    return logging.getLogger(name)
