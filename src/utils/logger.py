import logging

class Logger:
    """Logging class

    Attributes:
        logger (logging.Logger): Logger instance

    Methods:
        get_log_level: Get log level from string
        get_logger: Get logger instance
    """
    def __init__(self, name: str, log_level="DEBUG", log_format=None, date_format=None):
        LOG_LEVEL = self.get_log_level(log_level)

        if log_format is None:
            log_format = "%(asctime)s - %(levelname)s: [ %(name)s ] %(message)s"
        if date_format is None:
            date_format = "%m/%d/%Y %I:%M:%S %p"

        logging.basicConfig(format=log_format, level=LOG_LEVEL, datefmt=date_format)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(LOG_LEVEL)

    def get_log_level(self, level: str) -> int:
        """Get log level from string"""
        log_levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }
        return log_levels.get(level, logging.DEBUG)

    def get_logger(self) -> logging.Logger:
        return self.logger