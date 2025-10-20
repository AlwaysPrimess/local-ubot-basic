from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def weather_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}weather"):
            args = event.text.split(maxsplit=1)
            city = args[1] if len(args) > 1 else "Jakarta"
            await event.reply(f"🌤 Cuaca di **{city}** saat ini: Cerah (dummy).")
