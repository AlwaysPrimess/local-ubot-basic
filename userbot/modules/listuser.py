# userbot/modules/listuser.py

from telethon import events
import json
import os

# Lokasi database user yang dipakai oleh bot
DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    '..', 'bot', 'database.json'
)

OWNER_ID = 6976551745  # ID Owner sesuai permintaan

def load_users():
    """Memuat data user dari database.json"""
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, 'r') as f:
        try:
            data = json.load(f)
        except Exception:
            data = []
    return data


def register(client):
    """
    Fungsi ini dipanggil dari ubot.py agar event handler
    di dalam modul dihubungkan ke userbot.
    """

    @client.on(events.NewMessage(pattern=r'^\.listuser$'))
    async def handler_listuser(event):
        # Pastikan hanya owner yang bisa akses
        if event.sender_id != OWNER_ID:
            return await event.reply("❌ Kamu tidak diizinkan memakai perintah ini.")

        users = load_users()

        if not users:
            return await event.reply("🔍 Belum ada user yang terdaftar di database.")

        msg = "📋 **Daftar User Terdaftar:**\n"
        for i, u in enumerate(users, start=1):
            uid = u.get("id", "N/A")
            name = u.get("name", "Tidak diketahui")
            plan = u.get("plan", "N/A")
            msg += f"{i}. ID: `{uid}` | Nama: {name} | Plan: {plan}\n"

        await event.reply(msg)
