from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def tagall_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}tagall"):
            chat = await event.get_chat()
            if not getattr(chat, "participants_count", None):
                return await event.reply("❌ Hanya bisa di grup.")
            users = []
            async for user in event.client.iter_participants(chat):
                if user.username:
                    users.append(f"@{user.username}")
                else:
                    users.append(f"[{user.first_name}](tg://user?id={user.id})")
            text = "👥 Tagall:\n" + " ".join(users)
            await event.reply(text, link_preview=False)
