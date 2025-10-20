# listuser.py
from telethon import events

# Contoh database user sementara
USERS = [
    {"id": 12345, "name": "User1"},
    {"id": 67890, "name": "User2"},
]

def register(client):
    @client.on(events.NewMessage(pattern=r"\.listuser"))
    async def listuser_handler(event):
        if not USERS:
            await event.reply("❌ Tidak ada user terdaftar.")
            return
        
        msg = "👥 **Daftar User Terdaftar:**\n"
        for user in USERS:
            msg += f"- `{user['id']}` | {user['name']}\n"
        
        await event.reply(msg)
