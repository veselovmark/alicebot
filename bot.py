# -*- coding: utf-8 -*-
import config
import telebot
import logic

bot = telebot.TeleBot(config.token)
'''
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    
@bot.message_handler(content_types=["text"])
def function_name(message):
    if message.text=='What is your name?':   
        bot.reply_to(message, "My name is Alice. I am an intelligent chatbot designed by Atlas")
    elif message.text=='Is milk healthy?':
        bot.reply_to(message, "Yes. Milk consumption is healthy")
    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
'''

@bot.message_handler(content_types=["text"])
def function_name(message):
    answer=logic.get_answer(message.text)
    bot.reply_to(message, answer)


if __name__ == '__main__':
    bot.polling(none_stop=True)
