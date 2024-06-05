from tkinter import *

root = Tk()

def clicked1():
    global button2

    button1.config(state=DISABLED)
    button2 = Button(root, text="Button 2", command=clicked2)
    button2.grid(row=1, column=0)

    myLabel = Label(root, text="Button 1 is pressed!").grid(row=2, column=0)

def clicked2():
    global button1

    button2.config(state=DISABLED)
    button1 = Button(root, text="Button 1", command=clicked1)
    button1.grid(row=0, column=0)

    myLabel = Label(root, text="Button 2 is pressed!").grid(row=2, column=0)

button1 = Button(root, text="Button 1", command=clicked1)
button1.grid(row=0, column=0)

button2 = Button(root, text="Button 2", command=clicked2)
button2.grid(row=1, column=0)

root.mainloop()
