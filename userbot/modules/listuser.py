from telethon import events
from .mod_06_prefix import get_prefix

USERS = [
    {"id": 12345, "name": "User1"},
    {"id": 67890, "name": "User2"},
]

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def listuser_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}listuser"):
            if not USERS:
                await event.reply("❌ Tidak ada user terdaftar.")
                return
            msg = "👥 **Daftar User Terdaftar:**\n"
            for user in USERS:
                msg += f"- `{user['id']}` | {user['name']}\n"
            await event.reply(msg)
