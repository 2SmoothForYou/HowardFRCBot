import telepot
import time
import emoji

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])


TOKEN  = '259115532:AAHav6iX1Kgo53ECfUOBQpjMbz_oIX9gFek'
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening...')

bot.sendMessage(209854694, emoji.snowman)

while 1:
    time.sleep(10)




