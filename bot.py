
"""
The main app logic.
"""

import telebot
import config

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.reply_to(message, message.text)


# Run

bot.polling(none_stop=True)
