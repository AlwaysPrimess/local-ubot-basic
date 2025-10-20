from telethon import events
from .mod_06_prefix import get_prefix

TARGET_CHATS = ["me"]  # Bisa dikembangkan ke semua chat/user

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def broadcast_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}broadcast "):
            msg = event.text[len(f"{prefix}broadcast "):]
            for chat in TARGET_CHATS:
                try:
                    await client.send_message(chat, msg)
                except Exception as e:
                    print(f"Error broadcast ke {chat}: {e}")
            await event.reply("✅ Broadcast selesai.")
