from tkinter import *
import sqlite3
import os


#Variable that opens "Accounts" database

    
#Variable that opens "Accounts" database



if os.path.exists("Accounts.db") == False:
    
    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()
    accTable = '''CREATE TABLE Users (

        name varchar(20),
        password varchar(100)
    )'''
    c.execute(accTable)
    conn.commit()
    conn.close()


def Register():
    global screen1
    
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
  

    Label(screen1, text = "Create account").pack()

    Label(screen1, text = "").pack()

    Label(screen1, text = "Username").pack()

    global Username
    Username = Entry(screen1, width = 30)
    Username.pack()
    

    Label(screen1, text = "Password").pack()

    global Password 
    Password = Entry(screen1, width = 30)
    Password.pack()
   

    Button(screen1, text = "Register", width = 10, height = 1, command = createAcc).pack()

def createAcc():
    existsLabel = Label(screen1, fg="red", text = "")
    
    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()

    findUser = ("SELECT * FROM Users WHERE name = ? AND password = ?")
    c.execute(findUser,[(Username.get()),(Password.get())])
    isUserTaken = c.fetchall()

    if isUserTaken:
        existsLabel = Label(screen1, fg="red", text = "User already exists")
        existsLabel.pack()

    else:

        c.execute("INSERT INTO Users (name,password) VALUES (:name, :password)",
        {
          'name' : Username.get(),
          'password' : Password.get()
        })

        Label(screen1, fg="green", text = "User created").pack()

        
   


    conn.commit()
    conn.close


def Login():
    screen2 = Toplevel(screen)
    screen2.title("Log in")
    screen2.geometry("300x250")
    

    Label(screen2, text = "Username").pack()

    global inputUsername
    inputUsername = Entry(screen2, width = 30)
    inputUsername.pack()
    

    Label(screen2, text = "Password").pack()

    global inputPassword 
    inputPassword = Entry(screen2, width = 30)
    inputPassword.pack()

    Button(screen2, text = "Log in", width = 10, height = 1, command = allAccounts).pack()

def logginIn():

    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()

   
    



def allAccounts():


    conn = sqlite3.connect("Accounts.db")

    c = conn.cursor()
    c.execute("SELECT * FROM Users")
    Accounts = c.fetchall()

    for account in Accounts:
        print(account[0], account[1])
    if inputUsername == c.execute("SELECT name FROM Users") and inputPassword == c.execute("SELECT password FROM Users"):
        print("nais")
    
    


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


