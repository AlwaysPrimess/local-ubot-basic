from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def help_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}help"):
            msg = f"""
🛠 **Daftar Perintah Userbot:**
- {prefix}help — Lihat bantuan
- {prefix}echo <text> — Kirim ulang teks
- {prefix}broadcast <pesan> — Kirim ke semua chat
- {prefix}premium — Cek status premium
- {prefix}listuser — Lihat daftar user
- {prefix}prefix <prefix> — Ganti prefix
- {prefix}share <text> — Share teks/reply
- {prefix}download — Download media reply
"""
            await event.reply(msg)
