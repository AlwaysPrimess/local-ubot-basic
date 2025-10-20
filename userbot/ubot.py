import os
import asyncio
import json
from telethon import TelegramClient, events

# Load config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
if not os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, 'w') as f:
        json.dump({"api_id": "", "api_hash": "", "session": ""}, f, indent=2)

with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

api_id = config.get("api_id")
api_hash = config.get("api_hash")
session_name = config.get("session")

if not api_id or not api_hash or not session_name:
    raise ValueError("Isi api_id, api_hash, dan session di config.json terlebih dahulu.")

client = TelegramClient(session_name, int(api_id), api_hash)

# Load modules
from .modules import (
    help_mod,
    echo,
    broadcast,
    premium,
    listuser
)

# Register handlers from each module
help_mod.register(client)
echo.register(client)
broadcast.register(client)
premium.register(client)
listuser.register(client)

async def main():
    await client.start()
    print("Userbot aktif dan berjalan...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
