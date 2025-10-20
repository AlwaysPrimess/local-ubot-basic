# mod_08_download.py
from telethon import events
import os

DOWNLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def register(client):
    @client.on(events.NewMessage(pattern=r"\.download"))
    async def download_media(event):
        reply = await event.get_reply_message()
        if not reply or not reply.media:
            return await event.reply("❌ Reply ke media untuk mendownload.")

        file_path = await reply.download_media(file=DOWNLOAD_FOLDER)
        await event.reply(f"✅ Media berhasil didownload:\n`{file_path}`")
