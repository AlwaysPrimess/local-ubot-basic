from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def sticker_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}sticker"):
            reply = await event.get_reply_message()
            if not reply or not reply.media:
                return await event.reply("❌ Reply ke foto/video untuk convert sticker.")
            await event.reply("✅ (Dummy) Sticker berhasil dibuat dari media reply.")
