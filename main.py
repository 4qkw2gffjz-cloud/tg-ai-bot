import os
import sys
import types

# фикс для Python 3.13
sys.modules['imghdr'] = types.ModuleType('imghdr')

from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # мы добавим позже

app = FastAPI()
tg_app = ApplicationBuilder().token(TOKEN).build()


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот жив 👋")


tg_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))


@app.on_event("startup")
async def on_startup():
    await tg_app.initialize()
    await tg_app.bot.set_webhook(WEBHOOK_URL)
    await tg_app.start()
    print("Webhook установлен")


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, tg_app.bot)
    await tg_app.process_update(update)
    return {"ok": True}


@app.get("/")
def healthcheck():
    return {"status": "ok"}
