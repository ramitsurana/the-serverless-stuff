"""Utility module for logging."""
import logging
import os
from util.common_constants import Constants, EnvironmentVariables


class LoggerUtility:
    """Utility class for logging."""

    @staticmethod
    def set_level():
        """Set log level."""
        log_format = '%(asctime)-15s %(levelname)s:%(message)s'
        logging.basicConfig(format=log_format)
        logger = logging.getLogger(Constants.LOGGER_NAME)
        # Set Log level based on environment variable value
        try:
            log_level = os.environ[EnvironmentVariables.LOG_LEVEL]
        except KeyError:
            log_level = Constants.DEFAULT_LOG_LEVEL

        logger.setLevel(logging.getLevelName(log_level))
        return True

    @staticmethod
    def log_info(message):
        """Print INFO log."""
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.info('%s', message)
        return True

    @staticmethod
    def log_error(message):
        """Print ERROR log."""
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.error('%s', message)
        return True

    @staticmethod
    def log_warning(message):
        """Print WARNING log."""
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.warning('%s', message)
        return True

    @staticmethod
    def log_debug(message):
        """Print DEBUG log."""
        logger = logging.getLogger(Constants.LOGGER_NAME)
        logger.debug('%s', message)
        return True
