import perms
import sys

class functions:
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


	def c_stopbot(bot, msg):
		bot.sendMessage(msg['chat']['id'], "Shutting down bot...", disable_notification=True)
		bot.sendSticker(msg['chat']['id'],'BQADBAADFAIAAnpiZAWUDmg80U6hfgI', disable_notification=True)
		main.exit()
	