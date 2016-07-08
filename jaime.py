import telepot
import main
import unicode
def update(msg):
    content_type, chat_type, chat_id,  = telepot.glance(msg)
    if content_type == 'text':
        message = msg['text']
        #checks if text is equal to 'hi howard, how are you?', ignoring case
        if message.lower() == 'hi howard, how are you?'.lower():
            #replies to message
            main.bot.sendMessage(chat_id, "I'm doing just fine, thanks.")
        if message.lower() == 'shut up howard'.lower():
            main.bot.sendMessage(chat_id, unicode.het)
        if message.lower() == 'linnea'.lower():
            main.bot.sendMessage(chat_id, '*Linnea' + unicode.crown)