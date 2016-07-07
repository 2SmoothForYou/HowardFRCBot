import telepot
from pprint import pprint

bot = telepot.Bot('259115532:AAHav6iX1Kgo53ECfUOBQpjMbz_oIX9gFek')

response = bot.getUpdates(offset = 100000001)
bot.sendMessage(209854694, 'SUH DUDE')

pprint(response)
