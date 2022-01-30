import telebot
import random

nou = 200
m = 0
mm = 0
mmm = 0


bot = telebot.TeleBot('5249042094:AAFtQP2VwYyNP_Lij6G9RFk5hgHBRH86WKg')


@bot.message_handler(content_types=['text'])
def get_text_messages(message, nou=None, m=None, mm=None, a=None):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я бот Mohely. Я нужен для того чтобы ты мог делать мечи и продовать их.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет \nСделай малый меч")
    elif message.text == "Сделай малый меч":
        nou = nou - 50
        m = m + 1
        bot.send_message(message.from_user.id, "Хорошо, я с тебя возьму 50$. У тебя осталось ", str(nou) + "$")
    elif message.text == "Сделай средний меч":
        nou = nou - 100
        mm = mm + 1
        bot.send_message(message.from_user.id, "Хорошо, я с тебя возьму 100$. У тебя осталось ", str(nou) + "$")
    elif message.text == "Баланс":
        bot.send_message(message.from_user.id, str(nou) + "$")
    elif message.text == "Продай малый меч":
        a = random.randint(40,75)
        nou = nou + a
        bot.send_message(message.from_user.id, "Хорошо. У тебя его купили за ", str(a))
    elif message.text == "Продай малый меч":
        a = random.randint(80,150)
        nou = nou + a
        bot.send_message(message.from_user.id, "Хорошо. У тебя его купили за ", str(a))
    elif message.text == "Баланс мечей":
        bot.send_message(message.from_user.id, str(m), str(mm))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
