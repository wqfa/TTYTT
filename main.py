import telebot, os, time
bot = telebot.TeleBot('5393921528:AAEMpK64XMx3ALMeNIG82zjD2AhCjzMXowM')
while True:
    os.system("wget https://cataas.com/cat  --output-document=cat.jpg")
    bot.send_photo(chat_id="-1001208654752",photo=open('cat.jpg','rb'))
    time.sleep(10)
    
