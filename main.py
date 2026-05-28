import asyncio

from telethon import TelegramClient

from config import (
    API_ID,
    API_HASH,
    SESSION_NAME
)

from core.db import init_db
from core.commands import register_handlers


async def main():

    await init_db()

    client = TelegramClient(
        SESSION_NAME,
        API_ID,
        API_HASH
    )

    await client.start()

    me = await client.get_me()

    print(
        f"Запущен аккаунт: "
        f"{me.first_name}"
    )

    register_handlers(client)

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())