import json
import tkinter
import os
import comm
import index


with open('../logs/testlog.json') as json_file:
    data = json.load(json_file)
    bot = data['bot']['text']



# flag: true = bot
# flag: false = user
def update(flag, text):
    if(flag):
        return
    else:
        return
