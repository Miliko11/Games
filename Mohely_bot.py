import telebot

nou = 5


bot = telebot.TeleBot('5249042094:AAFtQP2VwYyNP_Lij6G9RFk5hgHBRH86WKg')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем могу помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "Спам":
        while nou >= 1:
            bot.send_message(message.from_user.id, "Я СПАМЕР.")
    elif message.text == "Как дела?":
        bot.send_message(message.from_user.id, "Отлично.")
    elif message.text == "Что ты умеешь?":
        bot.send_message(message.from_user.id, "Нечего. Только спамить тебе могу если захочешь.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
