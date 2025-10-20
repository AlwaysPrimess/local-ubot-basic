# mod_07_share.py
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"\.share(?: (.+))?"))
    async def share_text(event):
        reply = event.message.reply_to_msg_id
        text = event.pattern_match.group(1)

        if reply:
            replied_msg = await event.get_reply_message()
            await event.reply(f"📤 Share teks:\n{replied_msg.text}")
        elif text:
            await event.reply(f"📤 Share teks:\n{text}")
        else:
            await event.reply("❌ Gunakan .share <teks> atau reply pesan.")
