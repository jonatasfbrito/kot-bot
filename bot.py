import telebot
import json
import funcoes
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

boas = open("./textos/boasvindas.txt").read()
tokenbot = open("./config/token.txt").read()
txt_cmds = open("./textos/cmds.txt").read()

bot = telebot.TeleBot(tokenbot, parse_mode="MARKDOWN")

@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
	c_id = call.message.chat.id
	mid = call.message.message_id
	rtm = call.message.reply_to_message.message_id
	if call.data == "livros":
		mrk = InlineKeyboardMarkup()
		down = InlineKeyboardButton("DOWNLOAD",callback_data="download")
		mrk.add(down)
		bot.edit_message_text("Lista de livros didáticos",c_id,mid,reply_markup=mrk)
	if call.data == "apg":
		print(call)
		bot.delete_message(chat_id=c_id,message_id=mid)
		bot.delete_message(chat_id=c_id, message_id=rtm)
	if call.data == "comandos":
		mrk = InlineKeyboardMarkup()
		back = InlineKeyboardButton("Voltar",callback_data="voltar1")
		mrk.add(back)
		bot.edit_message_text(txt_cmds,c_id,mid, reply_markup=mrk)


@bot.message_handler(commands=['extenso'])
def extenso(message):
	arg = message.text
	try:
		arg1 = arg.split('/extenso')[1]
		ex = funcoes.Funcoes.numero_extenso(arg1)
		bot.reply_to(message, ex.upper())
	except:
		bot.reply_to(message, "*Ocorreu um erro...*")


@bot.message_handler(commands=['start'])
def start(message):
	markup = InlineKeyboardMarkup()
	livros = InlineKeyboardButton("Livros - PDF",callback_data="livros")
	cmds = InlineKeyboardButton("Comandos - Bot", callback_data="comandos")
	admin = InlineKeyboardButton("Desenvolvedor",url="t.me/kotzeraunix")
	src = InlineKeyboardButton("Source Code - Github",url="https://github.com/jonatasfbrito")
	markup.add(livros,cmds)
	markup.add(admin)
	markup.add(src)
	bot.reply_to(message, boas, reply_markup=markup)


@bot.message_handler(commands=['mensagem'])
def gerar(message):
	arg = message.text
	try:
		arg1 = arg.split('/mensagem')[1]
		res = funcoes.Funcoes.mensagem_autodestrutiva(arg1)
		linha = InlineKeyboardMarkup()
		apg = InlineKeyboardButton("Apagar",callback_data='apg')
		linha.add(apg)
		bot.reply_to(message, res, reply_markup=linha)
	except:
		bot.reply_to(message, "*Ocorreu um erro ao criar a mensagem.*\n_Possível causa: Voce não colocou a mensagem após o comando '/mensagem'._")

bot.infinity_polling()