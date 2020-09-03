from tkinter import *


root = Tk()

def myClick():
    napClik=Label(root, text="painettu", padx=30, pady=40, fg="green", bg="#CA934D")
    napClik.pack()

myButton = Button(root, text="Paina nappulaa")
myButton.pack()

myButton = Button(root, text="Paina nappulaa", padx=100, pady=50,command=myClick, fg="red", bg="#CA934D")
myButton.pack()

root.mainloop()