import telepot
import time
import jaime
import josh
import TOKEN

def handle(msg):
    content_type, chat_type, chat_id,  = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    jaime.update(msg)
    josh.update(msg)

bot = telepot.Bot(TOKEN.token)
bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)




