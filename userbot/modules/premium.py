# premium.py
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"\.premium"))
    async def premium_handler(event):
        # Nanti bisa dihubungkan dengan database
        await event.reply("💎 Status: *FREE USER*\nUpgrade segera untuk fitur Premium!")
