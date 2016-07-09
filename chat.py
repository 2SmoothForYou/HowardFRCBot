import perms


def c_test(bot, msg):
    bot.sendMessage(msg['chat']['id'], 'Test Message')


def c_me(bot, msg):
    bot.sendMessage(msg['chat']['id'],
                    'Username: @' + msg['from']['username'] +
                    '\nUser Id: ' + str(msg['from']['id']) +
                    '\nYou are: ' + perms.checkperms(msg['from']['id'],msg['chat']['id']))


def c_chat(bot, msg):
    bot.sendMessage(msg['chat']['id'],
                    'Current Chat: ' + msg['chat']['title'] +
                    '\nChat Id: ' + str(msg['chat']['id']))
