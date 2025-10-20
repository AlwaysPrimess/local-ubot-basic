import os
import asyncio
import json
from telethon import TelegramClient

# =======================
# CONFIG
# =======================
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

# Buat config jika belum ada
if not os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, 'w') as f:
        json.dump({"api_id": "", "api_hash": "", "session": "userbot"}, f, indent=2)

with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

api_id = config.get("api_id")
api_hash = config.get("api_hash")
session_name = config.get("session", "userbot")

if not api_id or not api_hash:
    raise ValueError("Isi api_id, api_hash di config.json terlebih dahulu!")

# =======================
# CLIENT
# =======================
client = TelegramClient(session_name, int(api_id), api_hash)

# =======================
# IMPORT MODUL
# =======================
from .modules import (
    help_mod,
    echo,
    broadcast,
    premium,
    listuser
)

# Import semua stub modul otomatis
for i in range(6, 51):
    mod_name = f"mod_{i:02}_stub"
    try:
        mod = __import__(f"userbot.modules.{mod_name}", fromlist=["register"])
        if hasattr(mod, "register"):
            mod.register(client)
    except Exception as e:
        print(f"Gagal load {mod_name}: {e}")

# Daftarkan modul aktif
help_mod.register(client)
echo.register(client)
broadcast.register(client)
premium.register(client)
listuser.register(client)

# =======================
# RUN USERBOT
# =======================
async def main():
    print("🔹 Userbot berjalan...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
