import main
import json

def checkPerms(user_id, chat_id):
	data = getPermsData()
	if chat_id not in data['user']['chat']:
		if user_id in data['user']['chat']['*']:
			level = data['user']['chat']['*'][user_id]['level']
		else:
			level = 'Default'
	else:
		if user_id not in data['user']['chat'][chat_id]:
			level = 'Default'
		else:
			data['user']['chat'][chat_id][user_id]['level']
	return level
	
def getPermsData():
	
	permsfile = open('FRCHowardBotPermissions.json','r')
	
	filecontents = permsfile.read()
	return json.loads(filecontents)
	
def runCommand(func,permname):
	data = getPermsData()
	if permname in data['permissions'][checkPerms(main.user_id, main.chat_id)]['commands'] or '*' in data['permissions'][checkPerms(main.user_id, main.chat_id)]['commands']:
		func()