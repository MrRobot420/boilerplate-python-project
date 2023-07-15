import json
from src.utils.logger import Logger
from builtins import FileNotFoundError, KeyError


class Loader:
    """Load all sort of things, like JSON from a file

    Attributes:
        None

    Methods:
        load_mock_json: Load a mock json file
    """

    def __init__(self):
        self.logger = Logger(__name__, "INFO").get_logger()
        self.base_dir = "tests/mock"

    def load_mock_json(self, variable_path: str, file="data.json"):
        """Load JSON data from a file by key(s)

        Args:
            key: Key of the credential
            file: JSON file to load
        """
        self.logger.info(f"🧲 Loading {variable_path} from file {file}...")
        try:
            keys = variable_path.split(".")
            with open(f"{self.base_dir}/{file}", "r") as file:
                file_content = json.load(file)
                for key in keys:
                    file_content = file_content[key]
                return file_content
        except (FileNotFoundError, KeyError) as e:
            self.logger.error(f"Error loading {variable_path} from {file}: {str(e)}")
