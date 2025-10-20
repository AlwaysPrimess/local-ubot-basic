# broadcast.py
from telethon import events

# Contoh list chat (bisa pakai database nanti)
TARGET_CHATS = ["me"]  # bisa ditambah ID chat, username, dll

def register(client):
    @client.on(events.NewMessage(pattern=r"\.broadcast (.+)"))
    async def broadcast_handler(event):
        msg = event.pattern_match.group(1)
        for chat in TARGET_CHATS:
            try:
                await client.send_message(chat, msg)
            except Exception as e:
                print(f"Error broadcast ke {chat}: {e}")
        await event.reply("✅ Broadcast selesai.")
