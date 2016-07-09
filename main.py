import telepot
import time
import unicode
import TOKEN
import perms
import chat


def handle(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
    print(content_type, chat_type, chat_id)
    jaimeID = 205253997
    joshID = 209854694
    howardID = 137028422

    if content_type == 'text':
        message = msg['text']
        id = msg['from']['id']
        input = message.upper()
        if '#TEST' in input:
            perms.runcommand(chat.c_test, msg, "test", msg)
        if '#ME' in input:
            perms.runcommand(chat.c_me, msg, "me", msg)
        if '#CHAT' in input:
            perms.runcommand(chat.c_chat, msg, "me", msg)
        if '@HOWARD_G' in input:
            bot.sendMessage(chat_id, 'Someone called for me?', reply_to_message_id=msg_id)
        if id == jaimeID and 'I' in input and 'LOVE' in input and 'JOSH' in input:
            bot.sendMessage(chat_id, "But don't tell Linnea" + unicode.crown + " " + unicode.wink,
                            reply_to_message_id=msg_id)
        if 'GET' in input and 'REKT' in input:
            bot.sendMessage(chat_id, 'DE_STROYED')
        if 'LINNEA' in input and 'LINNEA' + unicode.crown not in input and '@LINNEAW' not in input:
            bot.sendMessage(chat_id, '*Linnea' + unicode.crown, reply_to_message_id=msg_id)
        if 'HOWARD' in input:
            if 'HOW' in input and 'ARE' in input and 'YOU' in input:
                bot.sendMessage(chat_id, "I'm doing just fine, thanks.")
            if 'SHUT' in input and 'UP' in input:
                bot.sendMessage(chat_id, unicode.het)
            if 'JOKE' in input and 'TELL' in input:
                bot.sendMessage(chat_id,
                                'Once there was a snail who was tired of being slow. He went out and bought a really fast sports car and had the dealer paint a big S on each side of it. Whenever someone saw him zooming past in his new car, they would say, "Hey, look at that S-car go!"')
            if 'FUCK' in input and 'YOU' in input:
                bot.sendMessage(chat_id, 'no u', reply_to_message_id=msg_id)


TOKEN = TOKEN.token
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)


def getbot():
    return bot
