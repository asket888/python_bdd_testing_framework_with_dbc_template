import logging
from logging.config import fileConfig
from os import path

_PATH_TO_LOGIN_CONFIG = path.join(path.dirname(path.dirname(path.abspath(__file__))), "logging_config.ini")
fileConfig(_PATH_TO_LOGIN_CONFIG)
LOGGER = logging.getLogger()
