import json
import asyncio
import os
from telethon import TelegramClient, events
import importlib

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
# 4. Load Modules + Register
# =========================
def load_modules():
    modules_dir = "userbot/modules"
    for filename in os.listdir(modules_dir):
        if filename.endswith(".py") and filename not in ["__init__.py"]:
            mod_name = filename[:-3]
            try:
                module = importlib.import_module(f"userbot.modules.{mod_name}")
                if hasattr(module, "register"):
                    module.register(client)
                    print(f"[MODULE] Loaded: {mod_name}")
                else:
                    print(f"[MODULE] No register() in {mod_name}, skipped.")
            except Exception as e:
                print(f"[ERROR] Cannot load {mod_name}: {e}")

# =========================
# 5. Event Standar Help
# =========================
@client.on(events.NewMessage(pattern=f"^{PREFIX}help$"))
async def help_handler(event):
    await event.reply(
        f"✅ Userbot aktif.\n"
        f"Prefix saat ini: {PREFIX}\n"
        f"Ketik {PREFIX}modul, {PREFIX}echo, dll."
    )

async def main():
    await client.start()
    print("Userbot berjalan...")
    load_modules()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
