from tkinter import *
import sqlite3
import os


#Creates Accounts database if one does not exist yet
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

#Function that creates window where you can make an account
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
    Password = Entry(screen1, width = 30, show='*')
    Password.pack()
   
    global existsLabel
    existsLabel = Label(screen1, fg='red', text="")

    global tooSmall
    tooSmall = Label(screen1, fg="red", text="")

    Button(screen1, text = "Register", width = 10, height = 1, command = createAcc).pack()

    existsLabel.pack()

    
# Function checks if your account can be registered, it makes sure you dont make an 
# Account that has a password with less than 1 character or a name with less than tree characters
# It also doesent let you create an account if an account with the same name and password already exists
def createAcc():
    global existsLabel
    global tooSmall
    
    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()
    findUser = ("SELECT * FROM Users WHERE name = ? AND password = ?")
    c.execute(findUser,[(Username.get()),(Password.get())])
    isUserTaken = c.fetchall()

    if isUserTaken:
        existsLabel['text'] = "User already exists"

    else:
        if len(Username.get()) > 3 and len(Password.get()) >= 1:
            c.execute("INSERT INTO Users (name,password) VALUES (:name, :password)",
            {
            'name' : Username.get(),
            'password' : Password.get()
            })
            existsLabel['text'] = ""
            screen1.destroy()
           
        elif len(Password.get()) < 1:
            existsLabel['text'] = "Password must be atleast 1 character long"
        elif len(Username.get()) < 3:
            existsLabel['text'] = "Username must be atleast 3 characters long"

           

       
        
   


    conn.commit()
    conn.close

#This function creates a window where you can log in with you account
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
    inputPassword = Entry(screen2, width = 30, show='*')
    inputPassword.pack()

    Button(screen2, text = "Log in", width = 10, height = 1, command = logginIn).pack()
    Button(screen2, text = "Accounts", width = 10, height = 1, command = allAccounts).pack()

#This function checks what account you logged in with
def logginIn():

    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()

    findUser = ("SELECT * FROM Users WHERE name = ? AND password = ?")
    c.execute(findUser,[(inputUsername.get()),(inputPassword.get())])
    accountInput= c.fetchall()


    if accountInput:
        print("Logged in")





   
    



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


