from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

SESSION_NAME = os.getenv("SESSION_NAME")

DELAY_MIN = int(os.getenv("DELAY_MIN", 15))
DELAY_MAX = int(os.getenv("DELAY_MAX", 35))