from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def translate_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}tr "):
            text = event.text[len(f"{prefix}tr "):]
            # Dummy translate (bisa diganti API real)
            translated = text[::-1]
            await event.reply(f"🌐 Translasi (dummy):\n`{translated}`")
