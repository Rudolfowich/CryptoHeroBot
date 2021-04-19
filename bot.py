"""
The main app logic.
"""

import telebot
from telebot import types
import config
from cryptoParser import bnb_value, xrp_value

bot = telebot.TeleBot(config.TOKEN)

print(bnb_value())
print(xrp_value())


@bot.message_handler(content_types=['text'], commands=['start'])
def send_bnb(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_bnb = types.KeyboardButton(text='bnb')
    button_xrp = types.KeyboardButton(text='xrp')
    keyboard.add(button_bnb, button_xrp)
    bot.send_message(message.chat.id,
                     "Добро пожаловать в CryptoAlarmBot, в данном боте можно отслеживать курс актуальных криптовалют "
                     "и получать уведомления о коррекции/повышении/понижении курса. Выберете криптовалюту.",
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_bnb(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "xrp":
        xrp_price = bot.send_message(message.chat.id, f'Курс xrp на текущий момент {xrp_value()}$')
        bot.delete_message(message.chat.id, message.message_id)
    elif get_message_bot == "bnb":
        bnb_price = bot.send_message(message.chat.id, f'Курс bnb на текущий момент {bnb_value()}$')
        bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass


bot.polling()
