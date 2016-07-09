import json


def checkperms(user_id, chat_id):
    data = getpermsdata()
    if chat_id not in data['user']['chat']:
        if user_id in data['user']['chat']['*']:
            level = data['user']['chat']['*'][user_id]['level']
        else:
            level = 'Default'
    else:
        if user_id not in data['user']['chat'][chat_id]:
            level = 'Default'
        else:
            level = data['user']['chat'][chat_id][user_id]['level']
    return level


def getpermsdata():
    permsfile = open('FRCHowardBotPermissions.json', 'r')
    filecontents = permsfile.read()
    file_dump = json.loads(filecontents)
    return file_dump


def runcommand(func, options, permname, msg):
    data = getpermsdata()
    if permname in data['permissions'][checkperms(msg.user_id, msg.chat_id)]['commands'] or '*' in data['permissions'][checkperms(msg.user_id, msg.chat_id)]['commands']:
        func(*options)
