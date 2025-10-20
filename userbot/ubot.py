import json
import asyncio
from telethon import TelegramClient, events
import os

# =========================
# 1. Ambil API & Session
# =========================
with open('userbot/config.json', 'r') as f:
    api_data = json.load(f)

API_ID = api_data.get("api_id")
API_HASH = api_data.get("api_hash")
SESSION_NAME = api_data.get("session", "session_userbot")

# =========================
# 2. Ambil Prefix + Owner
# =========================
with open('userbot/database/config.json', 'r') as f:
    bot_data = json.load(f)

PREFIX = bot_data.get("prefix", ".")
OWNER_ID = bot_data.get("owner_id")

# =========================
# 3. Inisialisasi Client
# =========================
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# =========================
# 4. Load Modules Otomatis
# =========================
def load_modules():
    modules_dir = "userbot/modules"
    for filename in os.listdir(modules_dir):
        if filename.endswith(".py") and filename not in ["__init__.py"]:
            mod_name = filename[:-3]
            try:
                __import__(f"userbot.modules.{mod_name}")
                print(f"[MODULE] Loaded: {mod_name}")
            except Exception as e:
                print(f"[ERROR] Cannot load {mod_name}: {e}")

# =========================
# 5. Event Client Start
# =========================
@client.on(events.NewMessage(pattern=f"^{PREFIX}help$"))
async def help_handler(event):
    await event.reply("Userbot aktif.\nGunakan modul yang tersedia.\nPrefix saat ini: " + PREFIX)

async def main():
    await client.start()
    print("Userbot berjalan...")
    load_modules()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
