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
        input = message.upper()

        if 'LINNEA' in input and 'LINNEA' + unicode.crown not in input:
            bot.sendMessage(chat_id, '*Linnea' + unicode.crown)
        if 'HOWARD' in input:
            if 'HOW' in input and 'ARE' in input and 'YOU' in input:
                bot.sendMessage(chat_id, "I'm doing just fine, thanks.")
            if 'SHUT' in input and 'UP' in input:
                bot.sendMessage(chat_id, unicode.het)
            if 'JOKE' in input and 'TELL' in input:
                bot.sendMessage(chat_id, 'Once there was a snail who was tired of being slow. He went out and bought a really fast sports car and had the dealer paint a big S on each side of it. Whenever someone saw him zooming past in his new car, they would say, "Hey, look at that S-car go!"')

TOKEN  = TOKEN.token
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)



