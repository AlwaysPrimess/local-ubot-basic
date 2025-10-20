import time
from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def ping_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}ping"):
            start = time.time()
            msg = await event.reply("🏓 Pong...")
            end = time.time()
            latency = round((end - start) * 1000, 2)
            await msg.edit(f"🏓 Pong! `{latency} ms`")
