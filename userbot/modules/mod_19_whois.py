from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def whois_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}whois"):
            reply = await event.get_reply_message()
            if reply:
                target = await reply.get_sender()
            else:
                parts = event.text.split(maxsplit=1)
                if len(parts) < 2:
                    return await event.reply("❌ Reply atau pakai username/ID.")
                target = await event.client.get_entity(parts[1])

            info = (
                f"👤 **Info User**\n"
                f"ID: `{target.id}`\n"
                f"Nama: {target.first_name}\n"
                f"Username: @{target.username}\n"
            )
            await event.reply(info)
