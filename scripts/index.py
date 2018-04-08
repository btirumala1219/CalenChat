import tkinter
import csv
from tkinter import *
import json
import os
import comm
import updatetext

class testapphome(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.minsize(width=800, height=800)
        self.resizable(False,False)
        self.geometry(self.geometry())
        self.initialize()
        self.populate()

    def initialize(self):
        self.grid()

        # TEXT INPUT FRAME
        containerentry = tkinter.Frame(self, borderwidth=1, relief="sunken", width=475, height=100)
        containerentry.place(x=25, y=675)
        containerentry.grid_propagate(False)
        containerentry.grid_columnconfigure(0,weight=1)

        # TEXT INPUT BAR
        self.textinVariable = tkinter.StringVar()
        self.textinp = tkinter.Text(containerentry, bd = 6, height = 4)
        self.textinp.grid(column=0,row=1,sticky='EW')
        #self.textinp.bind("<Return>", self.OnSendClick)
        #self.textVariable.set(u"Enter text here.")

        # TEXT OUTPUT FRAME
        containeroutpt = tkinter.Frame(self, borderwidth=1, relief="sunken", width=550, height=650)
        containeroutpt.place(x=25, y=25)
        containeroutpt.grid_propagate(False)
        containeroutpt.grid_columnconfigure(0,weight=1)

        # TEXT OUTPUT BAR
        self.textoutVariable = tkinter.StringVar()
        self.textout = tkinter.Text(containeroutpt, bd = 1, height = 32, bg = "light blue")
        self.textout.grid(column=0,row=1,sticky='EW')
        #self.textout.bind("<Return>", self.OnPressEnter)
        #self.textVariable.set(u"Enter text here.")

        # SEND BUTTON FRAME
        containersend = tkinter.Frame(self, borderwidth=1, relief="sunken", width=75, height=100)
        containersend.place(x=500, y=675)
        containersend.grid_propagate(False)
        containersend.grid_columnconfigure(0,weight=1)

        # SEND BUTTON
        sendbutton = tkinter.Button(containersend,text="SEND", command=self.OnSendClick, height=4, bg="light slate gray")
        sendbutton.grid(column=0,row=0, sticky="EW")

        # INFO BUTTON FRAME
        containerinfo = tkinter.Frame(self, borderwidth=1, relief="sunken", width=125, height=75)
        containerinfo.place(x=625, y=400)
        containerinfo.grid_propagate(False)
        containerinfo.grid_columnconfigure(0,weight=1)

        # INFO BUTTON
        infobutton = tkinter.Button(containerinfo,text="About App", command=self.OnAboutClick, height=3)
        infobutton.grid(column=0,row=0, sticky="EW")

        # QUIT BUTTON FRAME
        containerquit = tkinter.Frame(self, borderwidth=1, relief="sunken", width=125, height=75)
        containerquit.place(x=625, y=500)
        containerquit.grid_propagate(False)
        containerquit.grid_columnconfigure(0,weight=1)

        # QUIT BUTTON
        quitButton = tkinter.Button(containerquit, text="Quit",command=self.quit, height=3)
        quitButton.grid(row=0, column=0, sticky="EW")

        # SAVE BUTTON FRAME
        containersave = tkinter.Frame(self, borderwidth=1, relief="sunken", width=125, height=75)
        containersave.place(x=625, y=100)
        containersave.grid_propagate(False)
        containersave.grid_columnconfigure(0,weight=1)

        # SAVE BUTTON
        savebutton = tkinter.Button(containersave,text="Save", command=self.writeToCSV, height=3)
        savebutton.grid(column=0,row=0, sticky="EW")

        # CLEAR BUTTON FRAME
        containerclear = tkinter.Frame(self, borderwidth=1, relief="sunken", width=125, height=75)
        containerclear.place(x=625, y=300)
        containerclear.grid_propagate(False)
        containerclear.grid_columnconfigure(0,weight=1)

        # CLEAR BUTTON
        savebutton = tkinter.Button(containerclear,text="Clear", command=self.clearText, height=3)
        savebutton.grid(column=0,row=0, sticky="EW")

        # LOAD BUTTON FRAME
        containerload = tkinter.Frame(self, borderwidth=1, relief="sunken", width=125, height=75)
        containerload.place(x=625, y=200)
        containerload.grid_propagate(False)
        containerload.grid_columnconfigure(0,weight=1)

        # LOAD BUTTON
        loadbutton = tkinter.Button(containerload,text="Load", command=self.loadData, height=3)
        loadbutton.grid(column=0,row=0, sticky="EW")

    def OnAboutClick(self):
        #print("check")
        os.system('about.py')

    def clearText(self):
        self.textout.delete("2.0", END)
        self.textout.insert(END,"\n")

    def OnSendClick(self):
        #print("enter testing")
        input = self.textinp.get("1.0",'end-1c')
        #print(input)
        self.addToText(input)
        self.commandCheck(input)
        self.textinp.delete("1.0", END)
        #self.populate()
        return

#       TODO:
#       We set initialize function to have 'Hello There' on boot
#       We need one function to be called that sends input text into json and updates field
#       We need one function that chooses the appropriate response and replies
#       Both of these functions can be called from here but best to be written in the comm.py file

    def populate(self):
        check = comm.load()
        botdata = check['bot']['text']
        userdata = check['user']['text']
        self.textout.insert(1.0,"Bot: " + botdata + "\n")


    def loadData(self):
        self.textout.delete("1.0", END)
        with open('../logs/test.csv', "rt") as csvfile:
            spamreader=csv.reader(csvfile)
            for row in spamreader:
                self.textout.insert(END, ', '.join(row))

    def addToText(self, text):
        self.textout.insert(END,"User: ")
        self.textout.insert(END ,text)
        self.textout.insert(END, "\n")

    def addToTextBot(self, text):
        self.textout.insert(END,"Bot: ")
        self.textout.insert(END ,text)
        self.textout.insert(END, "\n")

    def commandCheck(self, text):
        check = comm.checkCommand(text)
        #check what type of function this is
        self.addToTextBot(check)
        return

    def writeToCSV(self):
        filename = "../logs/test.csv"
        # opening the file with w+ mode truncates the file
        f = open(filename, "w+")
        f.close()
        with open('../logs/test.csv', 'a') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([self.textout.get("1.0",'end-1c')])

if __name__ == "__main__":
    app = testapphome(None)
    app.title('V1_APPTEST')
    app.mainloop()
