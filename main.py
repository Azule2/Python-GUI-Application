from tkinter import *

root = Tk()


#Label
myLabel1 = Label(root, text="Welcome to GUI IMine Small Apllication")
myLabel1.grid(row=1, column=0)

#def Rules
def myClick():
    myLabel = Label(root, text='1: Ugly speech is forbidden. \n 2:Doesn't attach to talk about P***.')
    myLabel.grid(row=2,column=0)

#button

btn_1 = Button(root, text='Discord Rules', padx=40, pady=3, command=myClick, fg="blue",bg="#1B2430")
btn_1.grid(row=3,column=0)

root.mainloop()
