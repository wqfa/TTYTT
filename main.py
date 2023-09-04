
#This bot is developed by Hamoudi AL-Amir ★
#Developer Channel | @MMMFi ✓.

import telebot
from telebot import types 

token = "6374219818:AAE0iUS7SWX5b6YHNEQbh_m13JI-Rwif-Ss"#توكنك
bot = telebot.TeleBot(token)
btn = types.InlineKeyboardButton(text='صانع الأساسي 𓅂', url = "https://t.me/C15CS")
@bot.message_handler(commands=["start"])
def start(message):
	brok = types.InlineKeyboardMarkup()
	brok.add(btn)
	bot.reply_to(message,text='- أهلاً بك عزيزي  في بوت كتابة اسمك على قميص اللاعبين مع اختيار رقم الاعب ✅                                             • ارسل اسمك ثم الرقم مثل alamir:7 💯',reply_markup=brok)

@bot.message_handler(content_types=['text'])
def fo(message):
	try:
		msg = message.text
		num = msg.split(':')[1]
		name = msg.split(':')[0]
		url = f'https://footballshirtmaker.com/en/spain/shirt-2021-II/number-{num}-{name}-001-square?v1200'
		bot.send_photo(message.chat.id,url)
	except:
		bot.reply_to(message,'- حدث خطأ ⚠️                                                • يرجى ارسال الاسم والرقم على النحو الآتي الرقم:الاسم ، مثل  alamir:7❗️')

bot.polling()
