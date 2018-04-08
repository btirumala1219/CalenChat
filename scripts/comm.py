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
    if "!print" in text:
        return 'You said print'
    if "me a joke" in text:
        x = random.randint(0,1)
        y = str(x)
        with open('../logs/jokes.json') as json_file:
            data = json.load(json_file)

            start = data[y]['text']
            return start
