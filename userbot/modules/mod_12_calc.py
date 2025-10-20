from telethon import events
from .mod_06_prefix import get_prefix

def register(client):
    @client.on(events.NewMessage(pattern=r".*"))
    async def calc_handler(event):
        user_id = event.sender_id
        prefix = get_prefix(user_id)
        if event.text.startswith(f"{prefix}calc "):
            expr = event.text[len(f"{prefix}calc "):]
            try:
                result = eval(expr, {"__builtins__": None}, {})
                await event.reply(f"🧮 Hasil: `{result}`")
            except:
                await event.reply("❌ Format salah. Contoh: .calc 2+3*5")
