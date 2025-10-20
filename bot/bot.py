import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from .utils import add_user, set_user_data, get_user_data

BOT_TOKEN = "8186046328:AAGqNJEZPXkjArIRFSnrWkY1nQT2-imSiWo"  # ganti token
OWNER_ID = 6976551745

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ENTER_API_ID, ENTER_API_HASH, ENTER_PHONE, ENTER_OTP = range(4)

# ========== HANDLER ==========
def start(update, context):
    user_id = update.effective_user.id
    add_user(user_id)
    keyboard = [
        [InlineKeyboardButton("Buat Userbot", callback_data="buat_ubot")],
        [InlineKeyboardButton("Batal", callback_data="cancel")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Cobain Userbot Trial 12 Hari Sekarang!!", reply_markup=reply_markup)

def callback_handler(update, context):
    query = update.callback_query
    query.answer()
    if query.data == "buat_ubot":
        query.message.reply_text("Masukkan API_ID kamu:", reply_markup=ReplyKeyboardRemove())
        return ENTER_API_ID
    elif query.data == "cancel":
        query.message.reply_text("Dibatalkan.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

def enter_api_id(update, context):
    api_id = update.message.text.strip()
    user_id = update.effective_user.id
    set_user_data(user_id, "api_id", api_id)
    update.message.reply_text("Masukkan API_HASH kamu:")
    return ENTER_API_HASH

def enter_api_hash(update, context):
    api_hash = update.message.text.strip()
    user_id = update.effective_user.id
    set_user_data(user_id, "api_hash", api_hash)
    update.message.reply_text("Masukkan nomor telepon kamu (format +62xxx):")
    return ENTER_PHONE

def enter_phone(update, context):
    phone = update.message.text.strip()
    user_id = update.effective_user.id
    set_user_data(user_id, "phone", phone)

    update.message.reply_text("Mencoba membuat session...")

    # generate session
    user = get_user_data(user_id)
    api_id = int(user['api_id'])
    api_hash = user['api_hash']
    session_file = os.path.join(os.path.dirname(__file__), f"{user_id}_session")
    client = TelegramClient(session_file, api_id, api_hash)

    async def start_client():
        await client.start(phone)
        try:
            me = await client.get_me()
            set_user_data(user_id, "session", f"{session_file}.session")
            await client.disconnect()
            await update.message.reply_text(f"✅ Userbot siap! Session tersimpan.\nID: {me.id}\nUsername: {me.username}")
        except SessionPasswordNeededError:
            await update.message.reply_text("Masukkan kode 2FA jika diminta di aplikasi Telegram.")
            await client.disconnect()

    import asyncio
    asyncio.run(start_client())
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text("Dibatalkan.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

# ========== MAIN ==========
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ENTER_API_ID: [MessageHandler(Filters.text & ~Filters.command, enter_api_id)],
            ENTER_API_HASH: [MessageHandler(Filters.text & ~Filters.command, enter_api_hash)],
            ENTER_PHONE: [MessageHandler(Filters.text & ~Filters.command, enter_phone)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CallbackQueryHandler(callback_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
