from telethon.tl.functions.messages import (
    GetDialogFiltersRequest
)

from core.db import add_chat


async def get_folders(client):

    response = await client(
        GetDialogFiltersRequest()
    )

    result = []

    for folder in response.filters:

        if not hasattr(folder, "id"):
            continue

        result.append({
            "id": folder.id,
            "title": folder.title
        })

    return result


async def import_folder(
    client,
    folder_id
):

    dialogs = await client.get_dialogs()

    imported = 0

    for dialog in dialogs:

        try:

            if dialog.folder_id != folder_id:
                continue

        except:
            continue

        chat = dialog.entity

        title = getattr(
            chat,
            "title",
            "Unknown"
        )

        await add_chat(
            chat.id,
            title
        )

        imported += 1

    return imported