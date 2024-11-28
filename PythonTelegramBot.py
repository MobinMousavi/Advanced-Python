#pip install python-telegram-bot

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}. How are you?')


app = ApplicationBuilder().token("YOUR_API_TOKEN").build()

app.add_handler(CommandHandler("start", hello))

app.run_polling()