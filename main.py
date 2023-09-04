from requests  		import *
from re  					import *
from telebot 			import *
from random			import *
from time  				import *
from datetime  		import datetime as dt
from string				import ascii_uppercase as uper 
from telebot.types   import InlineKeyboardMarkup as Mk
from telebot.types   import InlineKeyboardButton as btn
time = str(datetime.now()).rsplit(' ')[1].split('.')[0]
def user(num):
		a = ''.join(choice(uper)for i in range(1))
		b = ''.join(choice(uper)for i in range(1))
		c = ''.join(choice(uper)for i in range(1))
		d = ''.join(choice(uper)for i in range(1))
		return ''.join(choice(a+b+c+d)for i in range(num))
def user_():
	return choice(['_'.join(choice(uper)for i in range(3)), '_'.join(choice(uper)for i in range(4))])
def user_bot():
	return ''.join(choice(uper)for i in range(3))+"bot"
def check(user):
		res = get(f"https://t.me/{user}").text
		find= findall('<meta property="twitter:title" content="(.*?)">',res)[0].rsplit(" ",1)
		if find[0].strip() == 'Telegram: Contact' :
			return {'result':"ok" ,'user':user}
		else : return {'result':"nooo" ,'user':user} 

bot = TeleBot(("6374219818:AAE0iUS7SWX5b6YHNEQbh_m13JI-Rwif-Ss"))
key , cho , done = Mk()  , Mk() , Mk()
dev = btn(text="الصانع الاساسي ✓",url="t.me/C15CS") 
key.add(btn(text="بدء الصيد ★", callback_data="start"))
key.add(dev)
cho.add(
btn(text="خماسي",callback_data="5") , 
btn(text="أشباه",callback_data='_') ) 
cho.add(
btn(text="سباعي",callback_data="7") , 
btn(text="سداسي",callback_data="6"))
cho.add(btn(text="يوزر بوت ثلاثي",callback_data="bot"))
cho.add(dev)
@bot.message_handler(commands=['start'])
def start(message):
	text = """*أهلا بيك في بوت صيد معرفات Telegram
أختر من الازرار أدناه 👇🏻. *"""
	bot.send_message(message.chat.id,text,parse_mode="Markdown",reply_markup=key) 
@bot.callback_query_handler(func=lambda call:True)
def loop(call):
	good = 0
	bad = 0
	n = 0
	if call.data == "start":
		cho_typ = "*- أختر من أنواع المعرفات أدناه 👇🏻\nيوجد مبند !! *"
		bot.edit_message_text(chat_id=call.message.chat.id ,
		message_id=call.message.message_id,text = cho_typ , 
		parse_mode="Markdown",reply_markup=cho) 
	if call.data == '_':
		bot.answer_callback_query(call.id,
		"تم بدء صيد أشباه ✅")
		while True:
			us = user_() ; result = check(us)
			done = Mk()
			done.add(btn(text=us,callback_data="$"))
			done.add(
			btn(text=f"Good : {good}",callback_data="g"),
			btn(text=f"Bad : {bad}",callback_data="b"))
			done.add(dev)
			bot.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text= "*يتم الفحص الأن أنتظر .. *" , 
			parse_mode="Markdown",reply_markup=done)  
			if result['result'] == "ok" :
				good += 1
				sleep(0.7)
				txt_user = f"""*
 Telegram username . 
- - - - - - - - - - - - - - - - - - - - - - -
 username :- [ @{result['user']} ]
- - - - - - - - - - - - - - - - - - - - - - -
 Channel | @C15CS . *"""
				bot.send_message(call.message.chat.id,txt_user,parse_mode="Markdown")
			else:bad += 1;pass
			if good == 200:
				bot.send_message(call.message.chat.id,"Done ✅",
				parse_mode="Markdown")
				break
	if call.data == "5" :
		bot.answer_callback_query(call.id,
		"تم بدء صيد خماسي ✅")
		while True:
			us = user(5) ; result = check(us)
			done = Mk()
			done.add(btn(text=us,callback_data="$"))
			done.add(
			btn(text=f"Good : {good}",callback_data="g"),
			btn(text=f"Bad : {bad}",callback_data="b"))
			done.add(dev)
			bot.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text= "*يتم الفحص الأن أنتظر .. *" , 
			parse_mode="Markdown",reply_markup=done)  
			if result['result'] == "ok" :
				good += 1
				sleep(0.7)
				txt_user = f"""*
 Telegram username . 
- - - - - - - - - - - - - - - - - - - - - - -
 username :- [ @{result['user']} ]
- - - - - - - - - - - - - - - - - - - - - - -
 Channel | @C15CS . *"""
				bot.send_message(call.message.chat.id,txt_user,parse_mode="Markdown")
			else:bad += 1;pass
			if good == 200:
				bot.send_message(call.message.chat.id,"Done ✅",
				parse_mode="Markdown")
				break
	if call.data == "6":
		bot.answer_callback_query(call.id,
		"تم بدء صيد سداسي ✅")
		while True:
			us = user(6) ; result = check(us)
			done = Mk()
			done.add(btn(text=us,callback_data="$"))
			done.add(
			btn(text=f"Good : {good}",callback_data="g"),
			btn(text=f"Bad : {bad}",callback_data="b"))
			done.add(dev)
			bot.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text= "*يتم الفحص الأن أنتظر .. *" , 
			parse_mode="Markdown",reply_markup=done)  
			if result['result'] == "ok" :
				good += 1
				sleep(0.7)
				txt_user = f"""*
 Telegram username . 
- - - - - - - - - - - - - - - - - - - - - - -
 username :- [ @{result['user']} ]
- - - - - - - - - - - - - - - - - - - - - - -
 Channel | @C15CS . *"""
				bot.send_message(call.message.chat.id,txt_user,parse_mode="Markdown")
			else:bad += 1;pass
			if good == 200:
				bot.send_message(call.message.chat.id,"Done ✅",
				parse_mode="Markdown")
				break
	if call.data == "7":
		bot.answer_callback_query(call.id,
		"تم بدء صيد سباعي ✅")
		while True:
			us = user() ; result = check(us)
			done = Mk(7)
			done.add(btn(text=us,callback_data="$"))
			done.add(
			btn(text=f"Good : {good}",callback_data="g"),
			btn(text=f"Bad : {bad}",callback_data="b"))
			done.add(dev)
			bot.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text= "*يتم الفحص الأن أنتظر .. *" , 
			parse_mode="Markdown",reply_markup=done)  
			if result['result'] == "ok" :
				good += 1
				sleep(0.7)
				txt_user = f"""*
 Telegram username . 
- - - - - - - - - - - - - - - - - - - - - - -
 username :- [ @{result['user']} ]
- - - - - - - - - - - - - - - - - - - - - - -
 Channel | @C15CS . *"""
				bot.send_message(call.message.chat.id,txt_user,parse_mode="Markdown")
			else:bad += 1;pass
			if good == 200:
				bot.send_message(call.message.chat.id,"Done ✅",
				parse_mode="Markdown")
				break
	if call.data == "bot":
		bot.answer_callback_query(call.id,
		"تم بدء صيد يوزر بوت ثلاثي ✅")
		while True:
			us = user_bot() ; result = check(us)
			done = Mk()
			done.add(btn(text=us,callback_data="$"))
			done.add(
			btn(text=f"Good : {good}",callback_data="g"),
			btn(text=f"Bad : {bad}",callback_data="b"))
			done.add(dev)
			bot.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text= "*يتم الفحص الأن أنتظر .. *" , 
			parse_mode="Markdown",reply_markup=done)  
			if result['result'] == "ok" :
				good += 1
				sleep(0.7)
				txt_user = f"""*
 Telegram username . 
- - - - - - - - - - - - - - - - - - - - - - -
 username :- [ @{result['user']} ]
- - - - - - - - - - - - - - - - - - - - - - -
 Channel | @C15CS . *"""
				bot.send_message(call.message.chat.id,txt_user,parse_mode="Markdown")
			else:bad += 1;pass
			if good == 200:
				bot.send_message(call.message.chat.id,"Done ✅",
				parse_mode="Markdown")
				break
bot.polling(True)
