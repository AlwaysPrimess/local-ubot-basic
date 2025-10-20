# mod_06_prefix.py
from telethon import events

# Default prefix
PREFIXES = {}

def register(client):
    @client.on(events.NewMessage(pattern=r"\.prefix (\S+)"))
    async def change_prefix(event):
        user_id = event.sender_id
        new_prefix = event.pattern_match.group(1)
        PREFIXES[user_id] = new_prefix
        await event.reply(f"✅ Prefix diganti menjadi: {new_prefix}")

def get_prefix(user_id):
    return PREFIXES.get(user_id, ".")  # default "."
