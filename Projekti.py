from tkinter import *
import sqlite3
import os
import random



#Creates Accounts database and 2 tables in it if one does not exist yet
if os.path.exists("Accounts.db") == False:
    
    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()

    #this table holds all the users names and the their passwords
    accTable = '''CREATE TABLE Users (
        ID integer PRIMARY KEY,
        name varchar(20),
        password varchar(100)
    )'''

    #this table holds all the users tasks
    TaskTable= '''CREATE TABLE userTasks (
        userOfTasks integer NOT NULL,
        taskName varchar(20),
        task varchar(1000),
        FOREIGN KEY(userOfTasks) REFERENCES Users(ID)
    )'''

    c.execute(accTable)
    c.execute(TaskTable)
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
    Button(screen1, text = "Register", width = 10, height = 1, command = createAcc, fg="green").pack()
    existsLabel.pack()

    
# Function checks if your account can be registered, it makes sure you dont make an account that has a password with less than 1 character or a name with less than tree characters
# It also doesent let you create an account if an account with the same name and password already exists
def createAcc():
    global existsLabel
    global tooSmall
    
    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()
    findUser = ("SELECT * FROM Users WHERE name = ? AND password = ?")
    c.execute(findUser,[(Username.get()),(Password.get())])
    isUserTaken = c.fetchall()

    
    #if isUserTaken is TRUE it gives you a error message does not make a new account
    if isUserTaken:
        existsLabel['text'] = "User already exists"
    
    #if the the inputted is atleast 3 characters long and password atleast 1 character long it registers the account to the Users table
    else:
        if len(Username.get()) > 3 and len(Password.get()) >= 1:
            c.execute("INSERT INTO Users (name,password) VALUES (:name, :password)",
            {
            'name' : Username.get(),
            'password' : Password.get()
            })
            existsLabel['text'] = ""
            screen1.destroy()
           
        elif len(Password.get()) <1:
            existsLabel['text'] = "Password must be atleast 1 character long"
        elif len(Username.get()) <= 2:
            existsLabel['text'] = "Username must be atleast 3 characters long"

    conn.commit()
    conn.close

#This function creates a window where you can log in with you account
def Login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Log in")
    screen2.geometry("300x250")

    global spammerKick 
    spammerKick = 0

    global errorLabel
    errorLabel = Label(screen2, text="",fg="red")
    errorLabel.pack()

    Label(screen2, text = "Username").pack()

    global inputUsername
    inputUsername = Entry(screen2, width = 30)
    inputUsername.pack()

    Label(screen2, text = "Password").pack()

    global inputPassword 
    inputPassword = Entry(screen2, width = 30, show='*')
    inputPassword.pack()

    Button(screen2, text = "Log in", width = 10, height = 1, command = logginIn, fg="green").pack()
    Button(screen2, text = "Accounts", width = 10, height = 1, command = allAccounts).pack()

#This function checks what account you logged in with
def logginIn():
    global errorLabel
    global spammerKick

    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()

    
    findUser = ("SELECT * FROM Users WHERE name = ? AND password = ?")
    c.execute(findUser,[(inputUsername.get()),(inputPassword.get())])
    accountInput= c.fetchall()

    #opens taskList if you logged in with an registered account
    if accountInput:
        
        openTaskList()
        screen.destroy()
    
    else:
        #kicks you out of log in window if you get the acc name or password wrong 20 times
        randomErrorMessage = random.randint(0,5)
        spammerKick += 1
        if spammerKick == 20:
            screen2.destroy()
            spammerKick=0
        else:

            #Gives a random error message if you dont try to log in with a non existing account
            if randomErrorMessage == 0:
                errorLabel['text'] = "Something went wrong"
            elif randomErrorMessage == 1:
                errorLabel['text'] = "Try again"
            elif randomErrorMessage == 2:
                errorLabel['text'] = "bruh"
            elif randomErrorMessage == 3:
                errorLabel['text'] = "hmmm something is wrong"
            elif randomErrorMessage == 4:
                errorLabel['text'] = "Check for spelling mistakes"
            elif randomErrorMessage == 5:
                errorLabel['text'] = "nope"

#Creates the TaskList screen 
def openTaskList():
    global taskscreen
    taskscreen = Tk()
    taskscreen.geometry("500x500")
    taskscreen.title("TaskList")

    
    Button(taskscreen, text="Log out", bg="lightGray", fg="blue",command= logOut).grid(row=0 ,column=0)
    
    Button(taskscreen, text="Create new task", bg="lightGray", fg="green", width=31).grid(row=0 ,column=1)

    Button(taskscreen, text="My tasks", bg="lightGrey", fg="green", width=31).grid(row=0, column=6)

    
    
   

def allAccounts():

    conn = sqlite3.connect("Accounts.db")

    c = conn.cursor()
    c.execute("SELECT * FROM Users")
    Accounts = c.fetchall()

    for account in Accounts:
        print(account[0], account[1], account[2])
        print("----------------------------")
    if inputUsername == c.execute("SELECT name FROM Users") and inputPassword == c.execute("SELECT password FROM Users"):
        print("nais")
#logs closes the TaskList screen and opens main menu        
def logOut():
    taskscreen.destroy()
    main_screen()
#Main menu
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Projekti")
    Label(text = "Log in", bg= "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Log in", height = "2", width = "30", command = Login).pack()
    Label(text ="").pack()
    Button(text = "Create a new account", height = "2", width = "30", command = Register).pack()
    Button(text ="hax", command= openTaskList).pack()
    screen.mainloop()


main_screen()





