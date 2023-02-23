import telebot
from pytube import YouTube

bot = telebot.TeleBot('5818425342:AAGSVw40Auls6tBudMARmNmbz_SSUklgO0Y')

@bot.message_handler(commands=['start'])
def start(message):
    chatid = message.chat.id  
    bot.send_message(chatid, 'Вітаю! Надішли посилання на відео з Ютубу, яке бажаєш завантажити')
    
@bot.message_handler(content_types=['text'])
def text(message):
    chatid = message.chat.id 
    if 'https://www.youtube.com/' in message.text:
        link = message.text
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        a = ys.download()
        bot.send_message(chatid, 'Ось твоє відео:')
        with open(a, 'rb') as file:
            bot.send_video(chatid, file)
    else:
        bot.send_message(chatid, 'Це не посилання на відео з Ютубу 😉')

bot.polling(none_stop=True)