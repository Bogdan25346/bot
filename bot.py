import os
from threading import Thread
from flask import Flask

# ----------------- БЛОК ДЛЯ RENDER (FLASK) -----------------
app = Flask('')


@app.route('/')
def home():
  return 'Bot is alive!'


def run():
  # Render автоматически передает номер порта через переменную окружения PORT
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)


def keep_alive():
  # Запускаем веб-сервер в отдельном потоке, чтобы он не мешал боту
  t = Thread(target=run)
  t.start()


# Запускаем сервер
keep_alive()
# -----------------------------------------------------------

# Твой основной код бота начинается ниже:
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ... (дальше идет твой привычный код бота)




from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Обробка команди /start та виведення кнопок
async def start(update: Update, context):
    keyboard = [
        ["інфа про бота", "мій телефон"],
        ["послать нахуй"],
        ["получить привітання"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "бажаю здоров'я! нажми на будь яку кнопку нище:", 
        reply_markup=reply_markup
    )

# Обробка натискань на кнопки
async def handle_buttons(update: Update, context):
    message_text = update.message.text

    if message_text == "інфа про бота":
        await update.message.reply_text(
            "Кажу чесно й відкрито: код для цього бота я благополучно спіздив, "
            "але вклав у нього багато своїх сил й часу і відредагував його під себе. "
            "З повагою, GLADIATOR. :)"
        )
    elif message_text == "мій телефон":
        await update.message.reply_text("багато хочеш")
    elif message_text == "послать нахуй":
        await update.message.reply_text("іди нахуй")
    elif message_text == "получить привітання":
        await update.message.reply_text("вітаю тебе! бажаю щастя, здоров’я, многії літа!")
    else:
        await update.message.reply_text("нажми на копку знизу")

def main():
    # Токен зчитується зі змінних оточення (на Render)
    # Якщо запускаєш локально на ПК — заміни на TOKEN = "твій_токен"
    TOKEN = ("8991292270:AAGJVJURSNvkBD7ICdHoKi8W6yPtO6tU02g")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    keep_alive()

    application.run_polling()

if __name__ == "__main__":
    main()