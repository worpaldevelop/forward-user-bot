import asyncio
import random

from telethon.errors import (
    FloodWaitError,
    ChatWriteForbiddenError,
    UserBannedInChannelError
)

from core.db import (
    get_chats,
    remove_chat
)

from config import (
    DELAY_MIN,
    DELAY_MAX
)


async def send_message(
    client,
    reply_message,
    status_message=None
):

    chats = await get_chats()

    success = 0
    failed = 0

    for chat_id, title in chats:

        try:
            await client.forward_messages(
                entity=chat_id,
                messages=reply_message
            )

            success += 1

        except FloodWaitError as e:

            print(f"FloodWait: {e.seconds}")

            await asyncio.sleep(e.seconds)

        except (
            ChatWriteForbiddenError,
            UserBannedInChannelError
        ):

            await remove_chat(chat_id)

            failed += 1

            continue

        except Exception as e:

            print(f"{title}: {e}")

            failed += 1

        if status_message:

            await status_message.edit(
                f"✅ Успешно: {success}\n"
                f"❌ Ошибок: {failed}"
            )

        delay = random.randint(
            DELAY_MIN,
            DELAY_MAX
        )

        await asyncio.sleep(delay)