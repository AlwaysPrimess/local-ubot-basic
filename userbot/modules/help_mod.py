# help_mod.py
from telethon import events

HELP_TEXT = """
🛠 **Daftar Perintah Userbot:**
- .help — Lihat bantuan
- .echo <text> — Kirim ulang teks
- .broadcast <pesan> — Kirim ke semua chat
- .premium — Cek status premium
- .listuser — Lihat daftar user
"""

def register(client):
    @client.on(events.NewMessage(pattern=r"\.help"))
    async def help_handler(event):
        await event.reply(HELP_TEXT)
