from tkinter import *
import sqlite3
import os


#Variable that opens "Accounts" database
conn = sqlite3.connect("Accounts.db")
    
#Variable that opens "Accounts" database

c = conn.cursor()

if os.path.exists("Accounts.db"):
    print("On jo olemassa")
else:
    accTable = '''CREATE TABLE Accounts (
        name varchar(20)
        password varchar(100)
    )'''
    


def Register():
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    

    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Create account").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username").pack()
    Entry(screen1, textvariable = username).pack()
    Label(screen1, text = "Password").pack()
    Entry(screen1, textvariable = password).pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = createAcc).pack()
    
    from login import Login, Register

def createAcc():

    '''INSERT INTO Accounts (name,password) VALUES (username,password)'''

def Login():
    print("swag")

0
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Projekti")
    Label(text = "Log in", bg= "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = Login).pack()
    Label(text ="").pack()
    Button(text = "Register", height = "2", width = "30", command = Register).pack()

    screen.mainloop()




main_screen()

#root = Tk()

#def myClick():
    #napClik=Label(root, text="painettu", padx=30, pady=40, fg="green", bg="#CA934D")
    #napClik.pack()

#myButton = Button(root, text="Paina nappulaa")
#myButton.pack()

#myButton = Button(root, text="Paina nappulaa", padx=100, pady=50,command=myClick, fg="red", bg="#CA934D")
#myButton.pack()
#root.mainloop()

