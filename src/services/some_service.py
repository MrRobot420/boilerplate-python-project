from src.config.settings import ORGANIZATION_ID, OPENAI_API_KEY
from src.utils.logger import Logger


class SomeService:
    def __init__(self) -> None:
        self.logger = Logger(__name__, "INFO").get_logger()
        self.organization_id = ORGANIZATION_ID
        self.api_key = OPENAI_API_KEY

    def print_some_service(self):
        self.logger.info(self.organization_id)
        self.logger.info(self.api_key)
