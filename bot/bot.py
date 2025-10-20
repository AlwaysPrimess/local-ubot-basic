import logging
from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    ConversationHandler
)
from .utils import (
    add_user,
    set_user_data,
    get_user,
    OWNER_ID
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ganti tokenmu di sini
BOT_TOKEN = "BOT_TOKEN_HERE"

(
    ENTER_API_ID,
    ENTER_API_HASH,
    ENTER_PHONE
) = range(3)


def start(update, context):
    user_id = update.effective_user.id
    add_user(user_id)
    text = "Cobain Userbot Trial 12 Hari Sekarang!!"
    keyboard = [
        [InlineKeyboardButton("Buat Userbot", callback_data="buat_ubot")],
        [InlineKeyboardButton("Batal", callback_data="cancel")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text, reply_markup=reply_markup)


def callback_handler(update, context):
    query = update.callback_query
    data = query.data
    query.answer()
    
    if data == "buat_ubot":
        query.message.reply_text(
            "Silakan masukkan API_ID kamu:",
            reply_markup=ReplyKeyboardRemove()
        )
        return ENTER_API_ID
    elif data == "cancel":
        query.message.reply_text("Dibatalkan.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END


def enter_api_id(update, context):
    api_id = update.message.text
    user_id = update.effective_user.id

    set_user_data(user_id, "api_id", api_id)
    update.message.reply_text("Sekarang masukkan API_HASH kamu:")
    return ENTER_API_HASH


def enter_api_hash(update, context):
    api_hash = update.message.text
    user_id = update.effective_user.id

    set_user_data(user_id, "api_hash", api_hash)

    keyboard = ReplyKeyboardMarkup(
        [["Kirim Nomor", "Batal"]],
        resize_keyboard=True
    )
    update.message.reply_text(
        "Silakan kirim nomor telepon kamu dengan tombol di bawah.",
        reply_markup=keyboard
    )
    return ENTER_PHONE


def enter_phone(update, context):
    text = update.message.text
    user_id = update.effective_user.id

    if text.lower() == "batal":
        update.message.reply_text("Dibatalkan.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    
    if text.lower() == "kirim nomor":
        update.message.reply_text(
            "Silakan kirim nomor dalam format kontak TEKAN LAMA -> KIRIM KONTAK.\n"
            "Nanti lanjut OTP."
        )
        update.message.reply_text("Setelah itu silakan masukkan kode OTP (pisah spasi).")
        # di next step user memasukkan OTP
        return ENTER_PHONE
    else:
        update.message.reply_text(
            "Format tidak sesuai. Gunakan tombol 'Kirim Nomor' atau 'Batal'."
        )
        return ENTER_PHONE


def cancel(update, context):
    update.message.reply_text("Dibatalkan.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


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
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CallbackQueryHandler(callback_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
