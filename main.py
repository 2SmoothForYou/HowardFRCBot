import telepot
import time
import unicode
import json

def handle(msg):
    content_type, chat_type, chat_id,  = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        message = msg['text']
        #checks if text is equal to 'hi howard, how are you?', ignoring case
        if message.lower() == 'hi howard, how are you?'.lower():
            #replies to message
            bot.sendMessage(chat_id, "I'm doing just fine, thanks.")
        if message.lower() == 'shut up howard'.lower():
            bot.sendMessage(chat_id, unicode.het)



TOKEN  = '259115532:AAHav6iX1Kgo53ECfUOBQpjMbz_oIX9gFek'
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)




