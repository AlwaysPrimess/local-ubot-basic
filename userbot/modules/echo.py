# echo.py
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"\.echo (.+)"))
    async def echo_handler(event):
        text = event.pattern_match.group(1)
        await event.reply(text)
