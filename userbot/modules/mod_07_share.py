from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def share_text(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}share"):
            reply = event.message.reply_to_msg_id
            text = event.text[len(f"{prefix}share "):] if len(event.text) > len(f"{prefix}share ") else None

            if reply:
                replied_msg = await event.get_reply_message()
                await event.reply(f"📤 Share teks:\n{replied_msg.text}")
            elif text:
                await event.reply(f"📤 Share teks:\n{text}")
            else:
                await event.reply("❌ Gunakan .share <teks> atau reply pesan.")
