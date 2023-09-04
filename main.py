import telebot,time,requests,re
from telebot import types as t

see = requests.Session()

der = telebot.TeleBot('6374219818:AAE0iUS7SWX5b6YHNEQbh_m13JI-Rwif-Ss')

@der.message_handler(commands=['start'])
def start(mes):
	d = t.InlineKeyboardButton(' dev 👨‍💻 ', url='t.me/C15CS')
	de = t.InlineKeyboardMarkup(row_width=2);de.add(d)
	na = mes.from_user.first_name
	acc = der.send_message(mes.chat.id,text=f'Welcome {na} ,\nthis bot made by dergham\n\nsend username:password', reply_markup=de)
	der.register_next_step_handler(acc,ax)
def ax(mes):
		ac = str(mes.text)
		try:
			user = ac.split(':')[0]
			pasw = ac.split(':')[1]
		except IndexError as error:ث
			der.send_message(mes.chat.id,text='عذرا عزيزي 📛\nلا يمكنك الارسال على هذه النحو')
			if not (':') in ac:
				return
		zo = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
		zh = '1234567890'
		import random
		us="".join(random.choice(zo)for i in range(6))
		ud="".join(random.choice(zo)for i in range(4))
		udm="".join(random.choice(zh)for i in range(4))
		ua=f'{us}/9.80 (Series 60; {us} {ud}/7.0.{udm}00/28.3445; U; en) Presto/2.8.119 Version/11.10'
		see.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent": ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
		
		p = see.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
	#print(p)
		
		dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pasw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
		
		see.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent": ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
		
		po = see.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
		
		kie = see.cookies.get_dict()
		
		if 'xs' and 'c_user' in kie:
			koe = f"datr={kie['datr']};sb={kie['sb']};vpd=v1%3B633x360x2;locale=ar_AR;m_pixel_ratio=2;fr={kie['fr']};c_user={kie['c_user']};xs={kie['xs']};m_page_voice={kie['c_user']};wd=360x633;"
			der.send_message(mes.chat.id,text=f'''<strong>
✅ Good Cookie Facebook 
---------------------------------------------
<code>{koe}</code>
---------------------------------------------
@DevEviI - @C35CS </strong>''', parse_mode='html')
		else:
			der.send_message(mes.chat.id,text='عذرا عزيزي 📛\nخطا في تسجيل الدخول الرجاء إعادة المحاولة لطفاً')
der.polling()
