from main import getbot

bot = getbot()


def c_test(msg):
    bot.sendMessage(msg['chat']['id'], 'Test Message')


def c_me(msg):
    bot.sendMessage(msg['chat']['id'],
                    'Username: ' + msg['from']['username'] +
                    '\nUser Id: ' + str(msg['from']['id']))


def c_chat(msg):
    bot.sendMessage(msg['chat']['id'],
                    'Current Chat: ' + msg['chat']['title'] +
                    '\nChat Id: ' + str(msg['chat']['id']))
