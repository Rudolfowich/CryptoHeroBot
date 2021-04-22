"""
The main app logic.
"""
import time
from datetime import datetime
import telebot
from telebot import types
import config
from cryptoParser import bnb_value, xrp_value

bot = telebot.TeleBot(config.TOKEN)

print(bnb_value())
print(xrp_value())


def timenow():
    while True:
        now = datetime.now()
        dt_string = now.strftime("%H:%M")
        if (dt_string == "13:30"):
            time.sleep(60)
            return dt_string
        break


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
    chat_id = config.my_id
    bot.send_message(message.chat_id, 'Wake up!')


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


bot.polling(none_stop=True)
