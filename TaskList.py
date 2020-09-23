from tkinter import *
import sqlite3
import os


if os.path.exists("Accounts.db") == False:
    
    conn = sqlite3.connect("Accounts.db")
    c = conn.cursor()
    accTable = '''CREATE TABLE Tasks(

        taskN varchar(20),
        taskDescription varchar(500)
        
    )'''
    c.execute(accTable)
    conn.commit()
    conn.close()





def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("TaskList")

    button(screen, text="checkTables", command=checkTables).pack

    


    screen.mainloop()




main_screen()
