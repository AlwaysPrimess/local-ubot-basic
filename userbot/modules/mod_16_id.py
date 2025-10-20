from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def id_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}id"):
            reply = await event.get_reply_message()
            if reply:
                uid = reply.sender_id
                await event.reply(f"🆔 ID User Reply: `{uid}`")
            else:
                await event.reply(f"🆔 ID Kamu: `{user_id}`")
