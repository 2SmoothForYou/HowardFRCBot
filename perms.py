import json


def checkperms(user_id, chat_id):
    data = getpermsdata()
    chatid = str(chat_id)
    userid = str(user_id)
    if chatid not in data['user']['chat']:
        level = 'Default'
    else:
        if userid not in data['user']['chat'][chatid]:
            level = 'Default'
        else:
            level = data['user']['chat'][chatid][userid]['level']
    if userid in data['user']['chat']['*']:
        level = data['user']['chat']['*'][userid]['level']
    return level


def getpermsdata():
    permsfile = open('FRCHowardBotPermissions.json', 'r')
    filecontents = permsfile.read()
    file_dump = json.loads(filecontents)
    return file_dump


def runcommand(func, options, permname, msg):
    data = getpermsdata()
    print(data['user']['chat']['Howard Bot Testing']['181446813']['name'])
    print(checkperms(msg['from']['id'], msg['chat']['id']))
    print('User id: ' + str(msg['from']['id']))
    if permname in data['permissions'][checkperms(msg['from']['id'], msg['chat']['id'])]['commands'] or '*' in data['permissions'][checkperms(str(msg['from']['id']), msg['from']['id'])]['commands']:
        func(options)


#   Welcome to the super magical explaination box :D
#   When you originally run a command, you use runcommand()
#     Args:
#       func - The function that will be run if permissions are correct
#       options - Any options that might be used for the function
#       permname - The name of the permission that is being searched for
#       msg - the object containing the message
#
#   Upon running this function, it will set the variable data to the result of getpermsdata()
#   -getpermsdata():
#     Sets the variable permsfile to the file FRCHowardBotPermissions.json in read mode
#     After that, it will set the varible filecontents to the result of reading the file
#     It then sets file_dump to be the parsed json file, allowing you to get the data from an array
#
#   Back to runcommand(), the program will check if the permission that is requested is in the following json structure:
#       Searching the data variable,
#           "permissions":{
#               checkperms():{
#                   "commands":[permissionName]
#                              }
#                         }
#
#   -checkperms():
#     sets the data variable to the result of getpermsdata() (YES I KNOW ITS WASTEFUL)
#     checks if the chat id does not exist in the json file
#     if the chat id doesn't exist:
#       check if the user id exists in the json file under the id *
#       if the user id does exist:
#         set the level variable to the json value for user's level
#       if the user id does not exist:
#         set the level variable to Default
#     if the chat id does exist:
#       check if the user id exists in the chat_id folder
#       if the user id doesn't exist:
#         set the level variable to Default
#       if the user id does exist:
#         set the level variable to the json value for user's level in that chat
#
#   Finally, if permname is exists in the permissions json for that permissions level,
#     OR if * exists in the permissions for that level:
#       run the function
