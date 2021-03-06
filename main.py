import telepot
import time
import unicode
import TOKEN
import perms
import chat
import howardinit
from howardinit import bcolors
import sys
import random
from chat import functions
#from howardos import app


# Handles all of the interactions with the bot
def handle(msg):
    # Collects info about the message sent, the type of message, type of chat, unique ID of chat, date of message, and unique id of message
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
    if content_type == 'text':
        print 'Chat ID: ', msg['chat']['id'], ', Username of sender: ', msg['from']['username'], ', Message Text: ', msg['text']
    elif content_type == 'photo':
        print 'Chat ID: ', msg['chat']['id'], ', Username of sender: ', msg['from']['username'], ', File ID: ', msg['photo']['file_id']
    elif content_type == 'sticker':
        print 'Chat ID: ', msg['chat']['id'], ', Username of sender: ', msg['from']['username'], ', File ID: ', msg['sticker']['file_id']
    elif content_type == 'video':
        print 'Chat ID: ', msg['chat']['id'], ', Username of sender: ', msg['from']['username'], ', File ID: ', msg['video']['file_id']
    
    # Storing ids as variables for now
    jaimeID = 205253997
    joshID = 209854694
    howardID = 137028422
    linneaID = 181446813

    # Checks if the message sent was a text message
    if content_type == 'text':

        # Stores the message as a variable
        message = msg['text']
        # Converts the whole message to upper case
        input = message.upper()

        # Collects unique id of person who sent message
        id = msg['from']['id']

        # Checks if certain conditions are met regardless of case, sometimes also checking for ID of person
        if 'SDDS' in input:
            bot.sendMessage(chat_id, 'Are you having a stroke?', reply_to_message_id=msg_id)
        if '#STOPBOT' in input:
            perms.runcommand(functions.c_stopbot, (bot, msg), "stopbot", msg)
        if '#TEST' in input:
            perms.runcommand(functions.c_test, (bot, msg), "test", msg)
        if '#ME' in input:
            perms.runcommand(functions.c_me, (bot, msg), "me", msg)
        if '#CHAT' in input:
            perms.runcommand(functions.c_chat, (bot, msg), "me", msg)
        if 'DOGS' in input and 'BEST' in input and id != linneaID:
            bot.sendMessage(chat_id, '*Cats', reply_to_message_id=msg_id)
        if 'CATS' in input and 'SUCK' in input and id != linneaID:
            bot.sendMessage(chat_id, '*Dogs', reply_to_message_id=msg_id)
        if 'DOGS' in input and 'BEST' in input and id == linneaID:
            bot.sendMessage(chat_id, 'I agree!', reply_to_message_id=msg_id)
        if 'CATS' in input and 'SUCK' in input and id == linneaID:
            bot.sendMessage(chat_id, 'I agree!', reply_to_message_id=msg_id)
        if '@HOWARD_G' in input:
            bot.sendMessage(chat_id, 'Someone called for me?', reply_to_message_id=msg_id)
        if id == jaimeID and 'I' in input and 'LOVE' in input and 'JOSH' in input:
            bot.sendMessage(chat_id, "But don't tell Linnea" + unicode.crown + " " + unicode.wink,
                            reply_to_message_id=msg_id)
        if 'GET' in input and 'REKT' in input:
            bot.sendMessage(chat_id, 'DE_STROYED')
        if 'LINNEA' in input and 'LINNEA' + unicode.crown not in input and '@LINNEAW' not in input:
            bot.sendMessage(chat_id, '*Linnea' + unicode.crown, reply_to_message_id=msg_id)

        # Checks for if Howard was said because these are common phrases and we want to only include the ones with Howard
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


# Retrieves the token from token.py
TOKEN = TOKEN.token

# Initializes a connection with the Telegram API
bot = telepot.Bot(TOKEN)

# Loops handle function, checking for if conditions are met to cause an interaction
bot.message_loop(handle)

# Prints Logo in terminal
print
for i in howardinit.terminallogolarge:
    if i == ':':
        sys.stdout.write(bcolors.WARNING)
    else:
        sys.stdout.write(bcolors.OKGREEN)
    sys.stdout.write(i + bcolors.ENDC)
    sys.stdout.flush()
    time.sleep(.00001)
print
print
print('Preparing program for use...')
time.sleep(.5)
print('HowardBot is now activated. Scanning for messages.')

# Ensures the program doesn't end early
while 1:
    #app.loop()
    time.sleep(.1)
def exit():
  sys.exit(0)

def getbot():
    return bot
