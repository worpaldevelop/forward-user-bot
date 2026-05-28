from telethon import events

from core.db import (
    add_chat,
    get_chats
)

from core.sender import send_message


def register_handlers(client):

    @client.on(events.NewMessage(pattern=r"\.add"))
    async def add_chat_handler(event):

        chat = await event.get_chat()

        title = getattr(chat, "title", "Unknown")

        await add_chat(chat.id, title)

        await event.reply(
            f"✅ Чат добавлен:\n{title}"
        )


    @client.on(events.NewMessage(pattern=r"\.list"))
    async def list_handler(event):

        chats = await get_chats()

        if not chats:
            await event.reply("Список пуст")
            return

        text = "📋 Чаты:\n\n"

        for _, title in chats:
            text += f"• {title}\n"

        await event.reply(text)


    @client.on(events.NewMessage(pattern=r"\.send"))
    async def send_handler(event):

        reply = await event.get_reply_message()

        if not reply:

            await event.reply(
                "❌ Ответь на сообщение"
            )

            return

        status = await event.reply(
            "🚀 Рассылка запущена"
        )

        await send_message(
            client,
            reply,
            status
        )