import telebot
from Constant import TOKEN, MESSAGE
import time
from getters import *
from telebot import types


def main():
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def start(massage):
        text = MESSAGE['start'].format(massage.from_user.first_name)
        bot.send_message(massage.chat.id, text)
        time.sleep(1)
        markup = types.ReplyKeyboardMarkup()
        weather_kyiv = types.KeyboardButton('Київ')
        cat_but = types.KeyboardButton('Фото кота')
        odessa_but = types.KeyboardButton('Одеса')
        kharkiv_but = types.KeyboardButton('Харків')
        get_date_and_time = types.KeyboardButton('Дата і час')
        markup.row(weather_kyiv, cat_but, odessa_but, kharkiv_but, get_date_and_time)
        bot.send_message(massage.chat.id, MESSAGE['start_menu'], reply_markup=markup)

    @bot.message_handler()
    def second_menu(massage):
        text = massage.text
        if text.lower() == 'фото кота':
            path = open(get_cat_foto_link(), 'rb')
            bot.send_photo(massage.chat.id, path)
            path.close()
        elif text.lower() == 'дата і час':
            bot.send_message(massage.chat.id, get_time())
        else:
            bot.send_message(massage.chat.id, get_weather(text))

    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
