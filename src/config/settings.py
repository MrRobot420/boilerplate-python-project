import os
import dotenv

dotenv.load_dotenv()

ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
