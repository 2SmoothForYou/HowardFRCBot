import telepot
import time
import unicode
import json
import TOKEN

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
        if message.lower() == 'linnea'.lower():
            bot.sendMessage(chat_id, '*Linnea' + unicode.crown)
print('hi')
TOKEN  = TOKEN.token
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)



