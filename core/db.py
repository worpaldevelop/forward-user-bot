import aiosqlite

DB_PATH = "data/chats.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            chat_id INTEGER PRIMARY KEY,
            title TEXT
        )
        """)

        await db.commit()


async def add_chat(chat_id: int, title: str):
    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute(
            "INSERT OR IGNORE INTO chats VALUES (?, ?)",
            (chat_id, title)
        )

        await db.commit()


async def remove_chat(chat_id: int):
    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute(
            "DELETE FROM chats WHERE chat_id = ?",
            (chat_id,)
        )

        await db.commit()


async def get_chats():
    async with aiosqlite.connect(DB_PATH) as db:

        cursor = await db.execute(
            "SELECT chat_id, title FROM chats"
        )

        return await cursor.fetchall()