from telethon.errors import (
    FloodWaitError
)

from core.db import (
    get_chats,
    remove_chat
)

from core.antiflood import AntiFlood
from core.cleaner import BAD_ERRORS
from core.stats import Stats


async def send_message(
    client,
    reply_message,
    status_message=None
):

    antiflood = AntiFlood()

    stats = Stats()

    chats = await get_chats()

    for chat_id, title in chats:

        stats.current_chat = title

        try:

            await client.forward_messages(
                entity=chat_id,
                messages=reply_message
            )

            stats.success += 1

        except BAD_ERRORS:

            await remove_chat(chat_id)

            stats.deleted += 1

            continue

        except FloodWaitError as e:

            stats.floods += 1

            await antiflood.handle_flood(e)

            continue

        except Exception as e:

            print(f"{title}: {e}")

            stats.failed += 1

        if status_message:

            try:

                await status_message.edit(
                    stats.render()
                )

            except:
                pass

        await antiflood.wait()

    if status_message:

        await status_message.edit(
            "✅ Рассылка завершена\n\n"
            + stats.render()
        )