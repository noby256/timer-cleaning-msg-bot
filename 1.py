import telebot
import threading

bot = telebot.TeleBot('1397648319:AAETtYjdM6BeUHrdjkL4gUHeuy7nJgvRQkM')    

@bot.message_handler(commands=['start'])
def start_message(message):
    print('/start')
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler()
def message(message):
    print('msg: ' + str(message.date))
    threading.Timer(60 * 60, lambda: bot.delete_message(message.chat.id, message.message_id)).start()

print('polling')
bot.polling()

print('end')

