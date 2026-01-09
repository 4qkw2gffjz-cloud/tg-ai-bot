import sys
import types

# фикс для Python 3.13
sys.modules['imghdr'] = types.ModuleType('imghdr')

import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот жив 👋")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("Бот запущен")
    app.run_polling()


if __name__ == "__main__":
    main()
