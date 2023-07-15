import unittest
from src.utils.logger import Logger


class TestLogger(unittest.TestCase):
    """Test logger class

    Methods:
        test_get_log_level: Test if the log level is DEBUG
        test_info_level: Test if the log level is INFO
        test_warning_level: Test if the log level is WARNING
        test_error_level: Test if the log level is ERROR
        test_critical_level: Test if the log level is CRITICAL
    """

    def test_get_log_level(self):
        """Test if the log level is DEBUG"""
        self.logger = Logger(__name__, "DEBUG").get_logger()
        log_level = self.logger.getEffectiveLevel()
        self.assertEqual(log_level, 10)

    def test_info_level(self):
        """Test if the log level is INFO"""
        self.logger = Logger(__name__, "INFO").get_logger()
        log_level = self.logger.getEffectiveLevel()
        self.assertEqual(log_level, 20)

    def test_warning_level(self):
        """Test if the log level is WARNING"""
        self.logger = Logger(__name__, "WARNING").get_logger()
        log_level = self.logger.getEffectiveLevel()
        self.assertEqual(log_level, 30)

    def test_error_level(self):
        """Test if the log level is ERROR"""
        self.logger = Logger(__name__, "ERROR").get_logger()
        log_level = self.logger.getEffectiveLevel()
        self.assertEqual(log_level, 40)

    def test_critical_level(self):
        """Test if the log level is CRITICAL"""
        self.logger = Logger(__name__, "CRITICAL").get_logger()
        log_level = self.logger.getEffectiveLevel()
        self.assertEqual(log_level, 50)
