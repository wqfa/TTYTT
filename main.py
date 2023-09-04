import os
try:
	import telebot
	from telebot import types
	import requests
	import time
	import random,re
except ImportError:
	os.system('pip install telebot')
	os.system('pip install requests')
	os.system('pip install time')
	os.system('pip install random')
	os.system('pip install re')
	os.system('clear')
bot = telebot.TeleBot('6374219818:AAE0iUS7SWX5b6YHNEQbh_m13JI-Rwif-Ss')

@bot.message_handler(commands=['start','cookies'])
def st(message):
	but1 = types.InlineKeyboardButton('START - بدء', callback_data='but1')
	he = types.InlineKeyboardButton('HELP', callback_data='he')
	ur = types.InlineKeyboardButton('الصانع الاساسي', url='t.me/C15CS')
	mar = types.InlineKeyboardMarkup(row_width=2)
	mar.add(but1, he, ur)
	na = message.from_user.full_name
	bot.send_message(message.chat.id, text=f'''<strong>
اهلا بك {na} ،
البوت مخصص لسحب كوكيز انستا & فيسبوك
اضغط بدء لتشغيل البوت
</strong>
	''', parse_mode='html', reply_markup=mar)
@bot.callback_query_handler(func=lambda call:True)
def call1(call):
	if call.data == 'but1':
		t1 = types.InlineKeyboardButton('cookies & sessionid insta ', callback_data='t1')
		t2 = types.InlineKeyboardButton('cookies facebook', callback_data='t2')
		ch = types.InlineKeyboardButton(' channel', url='t.me/C15CS')
		ll = types.InlineKeyboardMarkup(row_width=2);ll.add(t1,t2,ch)
		nam = call.from_user.full_name
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
اهلا بك {nam} ،
اخِتر التطبيق لسحب الكوكيز
		''', reply_markup=ll)
	elif call.data == 'he':
		name = call.from_user.full_name
		idw = call.from_user.id
		user__name = call.from_user.username
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''
اهلا بك 
name ~ {name}
user ~ @{user__name}
id ~ <code>{idw}</code>
البوت مخصص لسحب كوكيز انستا و فيسبوك
الرجاء ارسال اليوزر مع الرمز علي هذه النحو
username:password
		''', parse_mode='html')
	elif call.data == 't1':
		de = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
رائع !!
ارسل اليوزر مع الباس على هذه النحو فضلا
username:password </strong>
		''', parse_mode='html')
		bot.register_next_step_handler(de, der)
	elif call.data == 't2':
		dee = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'''<strong>
رائع !!
ارسل اليوزر مع الباس على هذه النحو فضلا
username:password </strong>
		''', parse_mode='html')
		bot.register_next_step_handler(dee, derr)
def der(a):
	k = a.text
	try:
		user = k.split(':')[0]
		pasw = k.split(':')[1]
	except:
		bot.send_message(a.chat.id,text='عذرا عزيزي لا يمكنك الارسال على هذه النحو الرجاء راجع قسم المساعده')
		return
	if str(':') in k:
		url ='https://www.instagram.com/accounts/login/ajax/'
		head = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '336',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YPvYkQALAAH7ZlNgkXiBnW6y7AOy; ig_did=1C396C9B-7DC7-463E-A68B-FE991198F88A; ig_nrcb=1; shbid="944\0546317830362\0541658653745:01f7bf09c30c2bf6ae86e32af31b5991cd84a607e1547a0132f6b653c4b76ecc26abbc4e"; shbts="1627117745\0546317830362\0541658653745:01f716bcf5ca94c711aa8ee17e52cf927685a30c29c89e0310cfe9f86589901109fd5b1e"; rur="RVA\05448065200129\0541658659405:01f7d96b5f9c1cf2396b6d00cbc7281da4dc2bb4c75a035bf4917e188315d170aec60aa2"; csrftoken=mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'x-asbd-id': '437806',
        'x-csrftoken': 'mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
        'x-instagram-ajax': 'caee87137ae9',
        'x-requested-with': 'XMLHttpRequest'
    }
		tim = str(time.time()).split('.')[1]
		data = {
        'username': f'{user}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{pasw}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
    }
		rr = requests.post(url, headers=head,data=data).text
		print(rr)
		if ('"Sorry, your password was incorrect. Please double-check your password."') in rr or ('"user":true,"authenticated":false,') in rr:
			bot.send_message(a.chat.id,text='باسورد خطا')
		elif ('"checkpoint_url"') in rr:
			bot.send_message(a.chat.id,text='الحساب سكيور')
		elif ('"user":true,') and ('"authenticated":true,') in rr:
			oo = rr.cookies
			coo = rr.get_dict()
			cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
			sessoin = coo['sessionid']
			bot.send_message(a.chat.id,text=f'''
تسجيل دخول صحيح

cook ~ <code>{cookie}</code>

sessionid ~ <code>{sessoin}</code>
			''', parse_mode='html', reply_to_message_id=k)
	else:
		pass
def derr(s):
	l = s.text
	try:
		usee = s.split(':')[0]
		paso = s.split(':')[1]
	except:
		bot.send_message(s.chat.id,text='عذرا عزيزي لا يمكنك الارسال على هذه النحو الرجاء راجع قسم المساعده')
		return
	if str(':') in l:
		see = requests.Session()
		while True:
			zo ='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
			zh='1234567890'
			us="".join(random.choice(zo)for i in range(6))
			ud="".join(random.choice(zo)for i in range(4))
			udm="".join(random.choice(zh)for i in range(4))
			ua =f'{us}/9.80 (Series 60; {us} {ud}/7.0.{udm}00/28.3445; U; en) Presto/2.8.119 Version/11.10'
		see.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent": ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
		p = see.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
		dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":usee,"flow":"login_no_pin","pass":paso,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
		see.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent": ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
		po = see.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
		kie = see.cookies.get_dict()
		if 'xs' and 'c_user' in kie:
			koe = f"datr={kie['datr']};sb={kie['sb']};vpd=v1%3B633x360x2;locale=ar_AR;m_pixel_ratio=2;fr={kie['fr']};c_user={kie['c_user']};xs={kie['xs']};m_page_voice={kie['c_user']};wd=360x633;"
			bot.send_message(s.chat.id,text=f'''
good cookies

cookie = <code>{koe}</code>
			''', parse_mode='html', reply_to_message_id=l)
bot.polling(True)
