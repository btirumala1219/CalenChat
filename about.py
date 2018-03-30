import tkinter

file = open("about.txt", "r")
#print(file.read())
name = file.readline()
#print(name)
data = file.readline()
#print(data)

file.close()

class testabout(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.minsize(width=800, height=800)
        self.resizable(False,False)
        self.geometry(self.geometry())
        self.initialize()

    def initialize(self):
        self.grid()

        var = tkinter.StringVar()
        label = tkinter.Label(self, textvariable = var)
        var.set(name)
        label.grid(column=0,row=0)

        var1 = tkinter.StringVar()
        labell = tkinter.Label(self, textvariable = var1)
        var1.set(data)
        labell.grid(column=0,row=1)

        # QUIT BUTTON FRAME
        containerquit = tkinter.Frame(self, borderwidth=1, relief="sunken", width=125, height=75)
        containerquit.place(x=625, y=200)
        containerquit.grid_propagate(False)
        containerquit.grid_columnconfigure(0,weight=1)

        # QUIT BUTTON
        quitButton = tkinter.Button(containerquit, text="Quit",command=self.quit, height=3)
        quitButton.grid(row=0, column=0, sticky="EW")

if __name__ == "__main__":
    app = testabout(None)
    app.title('V1_APP')
    app.mainloop()
