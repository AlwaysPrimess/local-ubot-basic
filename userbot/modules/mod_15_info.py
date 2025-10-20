from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def info_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}info"):
            me = await event.client.get_me()
            await event.reply(f"👤 Nama: {me.first_name}\n🆔 ID: {me.id}\nUsername: @{me.username}")
