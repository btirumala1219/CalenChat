import json
import tkinter
import os
import updatetext
import index

def load():
    with open('../logs/testlog.json') as json_file:
        data = json.load(json_file)
        start = data['bot']['text']

    return data
