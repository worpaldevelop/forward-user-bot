from telethon import events

from core.db import (
    add_chat,
    get_chats
)

from core.sender import send_message

from core.folders import (
    get_folders,
    import_folder
)


def register_handlers(client):

    @client.on(events.NewMessage(pattern=r"\.start"))
    async def start_handler(event):
        
        await event.reply("Forward-user-bot")

    @client.on(events.NewMessage(pattern=r"\.folders"))
    async def folders_handler(event):

        folders = await get_folders(client)

        if not folders:

            await event.reply(
                "❌ Папки не найдены"
            )

            return

        text = "📂 Папки:\n\n"

        for folder in folders:

            text += (
                f"ID: {folder['id']} | "
                f"{folder['title']}\n"
            )

        await event.reply(text)

    @client.on(events.NewMessage(pattern=r"\.import (\d+)"))
    async def import_handler(event):

        folder_id = int(
            event.pattern_match.group(1)
        )

        msg = await event.reply(
            "📥 Импорт папки..."
        )

        imported = await import_folder(
            client,
            folder_id
        )

        await msg.edit(
            f"✅ Импортировано: {imported}"
        )
    
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