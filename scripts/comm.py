import json
import tkinter
import os
import updatetext
import index
import random
import datetime

now = datetime.datetime.now()
today = str(now.month)+"."+str(now.day)+"."+str(now.year)

def load():
    with open('../logs/testlog.json') as json_file:
        data = json.load(json_file)
        start = data['bot']['text']

    return data

def checkCommand(text):
    text=text.lower()
    if 'hi' in text or 'hello' in text:
        print(today)
        return ('What can I help you with?', 'TRUE')
    if "me a joke" in text:
        x = random.randint(0,2)
        y = str(x)
        with open('../logs/jokes.json') as json_file:
            data = json.load(json_file)
            start = data[y]['text']
            return (start, 'TRUE')
    if "have to do today" in text:
        with open('../logs/cal.json') as json_file:
            data = json.load(json_file)
            start = 'Today, you have ' + data[today]["name"] + ' at ' + data[today]["time"] + ' for ' + data[today]["duration"] + ". Would you like more details?"
            return (start, 'TRUE')
    if "what is today" in text:
        return ("Today is " + today, 'TRUE')
        #TODO: Figure out how to add to cal.json
    if "do you love me" in text:
        return("nahhh u ugly", 'TRUE')    
    else:
        return ("I couldnt understand what you said", 'TRUE')
