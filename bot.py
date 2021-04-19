"""
The main app logic.
"""

import telebot
import config
from cryptoParser import bnb_value

bot = telebot.TeleBot(config.TOKEN)

print(bnb_value())


@bot.message_handler(commands=['bnb', 'start'])
def send_welcome(message):

    msg = bot.send_message(message.chat.id, f'Курс bnb на текущий момент {bnb_value()}')



@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass


bot.polling()
