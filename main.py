import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Чё пялишься? Я вообще-то думаю 🤨")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Бот запущен")
app.run_polling()
