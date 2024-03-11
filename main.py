import telebot
from telebot import types
from conf import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def helloWorld(message):
    bot.reply_to(message, 'Hello world')
    
@bot.message_handler(commands=['help'])
def get_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('/start')
    button1 = types.KeyboardButton('/help')
    button2 = types.KeyboardButton('/buttons')
    markup.add(button, button1, button2)
    bot.send_message(message.chat.id,text='Все команды',  reply_markup=markup)

@bot.message_handler(commands=['buttons'])
def get_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Кнопка')
    markup.add(button)
    bot.send_message(message.chat.id, 'Кнопки', reply_markup=markup)

@bot.message_handler(content_types='text')
def get_hello(message):
    if message.text == 'Hello':
        bot.reply_to(message, 'HI')


bot.infinity_polling()
    
    