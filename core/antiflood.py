import asyncio
import random

from telethon.errors import FloodWaitError

from config import (
    BASE_DELAY,
    DELAY_JITTER,
    COOLDOWN_EVERY,
    COOLDOWN_TIME
)


class AntiFlood:

    def __init__(self):

        self.sent = 0

    async def wait(self):

        delay = (
            BASE_DELAY +
            random.randint(1, DELAY_JITTER)
        )

        await asyncio.sleep(delay)

        self.sent += 1

        if self.sent % COOLDOWN_EVERY == 0:

            print(
                f"Cooldown: {COOLDOWN_TIME}"
            )

            await asyncio.sleep(
                COOLDOWN_TIME
            )

    async def handle_flood(self, error):

        if isinstance(error, FloodWaitError):

            wait_time = error.seconds + 5

            print(
                f"FloodWait {wait_time}"
            )

            await asyncio.sleep(wait_time)

            return True

        return False