import json
import tkinter
import os
import updatetext
import index
import random

def load():
    with open('../logs/testlog.json') as json_file:
        data = json.load(json_file)
        start = data['bot']['text']

    return data

def checkCommand(text):
    text.lower()
    if 'hi' in text or 'hello' in text:
        return ('What can I help you with?', 'TRUE')
    if "me a joke" in text:
        x = random.randint(0,2)
        y = str(x)
        with open('../logs/jokes.json') as json_file:
            data = json.load(json_file)
            start = data[y]['text']
            return (start, 'TRUE')
    else:
        return ("I couldnt understand what you said", 'TRUE')
