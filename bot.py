import telebot
import json
import pprint
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

boas = open("./textos/boasvindas.txt").read()
tokenbot = open("./config/token.txt").read()

bot = telebot.TeleBot(tokenbot)

@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
	if call.data == "livros":
		c_id = call.message.chat.id
		mid = call.message.message_id
		mrk = InlineKeyboardMarkup()
		down = InlineKeyboardButton("DOWNLOAD",callback_data="download")
		mrk.add(down)
		bot.edit_message_text("Lista de livros didáticos",c_id,mid,reply_markup=mrk)

@bot.message_handler(commands=['start'])
def start(message):
	markup = InlineKeyboardMarkup()
	livros = InlineKeyboardButton("Livros - PDF",callback_data="livros")
	contato = InlineKeyboardButton("Grupo", url="t.me/grupo")
	admin = InlineKeyboardButton("Desenvolvedor",url="t.me/kotzeraunix")
	src = InlineKeyboardButton("Source Code - Github",url="https://github.com/jonatasfbrito")
	markup.add(livros,contato)
	markup.add(admin)
	markup.add(src)
	bot.reply_to(message, boas, reply_markup=markup)

bot.infinity_polling()