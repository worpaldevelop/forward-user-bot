from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

SESSION_NAME = os.getenv("SESSION_NAME")

DELAY_MIN = int(os.getenv("DELAY_MIN", 15))
DELAY_MAX = int(os.getenv("DELAY_MAX", 35))

BASE_DELAY = int(os.getenv("BASE_DELAY", 20))
DELAY_JITTER = int(os.getenv("DELAY_JITTER", 15))

COOLDOWN_EVERY = int(
    os.getenv("COOLDOWN_EVERY", 15)
)

COOLDOWN_TIME = int(
    os.getenv("COOLDOWN_TIME", 120)
)

MAX_RETRIES = int(
    os.getenv("MAX_RETRIES", 3)
)