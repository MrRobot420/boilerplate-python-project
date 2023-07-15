from src.services.some_service import SomeService
from src.utils.logger import Logger


class Main:
    """Main class

    Attributes:
        args: Arguments passed to the script

    Methods:
        main: Main method
    """

    def __init__(self):
        self.logger = Logger(__name__, "INFO").get_logger()
        self.service = SomeService()

    def main(self):
        """Main method"""
        self.logger.info("# STARTING %s...", "Boilerplate Project")
        self.service.print_some_service()

    def example(self):
        """Example method"""
        self.logger.info("Example method")


main = Main()

try:
    while True:
        main.main()
except KeyboardInterrupt:
    logger = Logger(__name__, "INFO").get_logger()
    logger.warning("🫡  OK, lol bye. 👋 Exiting...")
