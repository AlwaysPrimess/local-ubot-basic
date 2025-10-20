from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def premium_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}premium"):
            await event.reply("💎 Status: *FREE USER*\nUpgrade segera untuk fitur Premium!")
