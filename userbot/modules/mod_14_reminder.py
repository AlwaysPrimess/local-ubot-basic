from telethon import events
import asyncio
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def reminder_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}reminder "):
            args = event.text[len(f"{prefix}reminder "):].split(maxsplit=1)
            if len(args) < 2:
                return await event.reply("❌ Contoh: .reminder 10s Beli kopi")
            waktu, pesan = args
            try:
                if waktu.endswith("s"):
                    detik = int(waktu[:-1])
                elif waktu.endswith("m"):
                    detik = int(waktu[:-1]) * 60
                else:
                    return await event.reply("❌ Gunakan s/m. Contoh: 10s, 1m")
                await event.reply(f"⏳ Pengingat dibuat dalam {waktu}...")
                await asyncio.sleep(detik)
                await event.reply(f"🔔 Pengingat: {pesan}")
            except:
                await event.reply("❌ Format salah.")
