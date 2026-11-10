
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 👋\n"
        "به ربات تحلیل‌ریز خوش آمدی.\n\n"
        "نام نماد بورسی را ارسال کن تا درخواست تحلیل ثبت شود."
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = update.message.text.strip()
    await update.message.reply_text(
        f"درخواست تحلیل نماد {symbol} ثبت شد.\n"
        "به‌زودی موتور تحلیل تکنیکال به ربات متصل می‌شود."
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN تنظیم نشده است")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, analyze)
    )

    app.run_polling()

if __name__ == "__main__":
    main()
