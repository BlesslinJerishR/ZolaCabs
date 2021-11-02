import random
import time
import datetime
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

Item4 = 0

# Create a new DB if dir is 404 @startup

with sqlite3.connect('Users.db') as conn:
    conn.cursor()
    
conn.execute('CREATE TABLE IF NOT EXISTS user (username TEXT not NULL, password TEXT not NULL')
conn.commit()
conn.close()

# main
class User:
    def __init__(self, master):
        # window
        self.master = master
        # some useful stuff
        self.username = StringVar()
        self.password = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        # widgets++ stuff
        self.widgets()
        
        # Logins
        def login(self):
            # Establish DB connection
            with sqlite3.connect('Users.db') as conn:
                conn.cursor()
                
            # Fetch users
            find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
            conn.execute(find_user, [self.username.get(), self.password.get()])
            result = conn.fetchall()
            if result:
                self.logf.pack_forget()
                self.head['text'] = "Welcome to Zola Cabs "+ self.username.get()
                self.head.configure(fg="black")
                self.head.pack(fill=X)
                application = travel(root)
            else:
                msg.showerror('oops' ,'Username not found.')
        
        # user++
        def new_user(self):
            # Establish connection
            with sqlite3.connect('User.db') as conn:
                conn.cursor()
                
            # username Exists
            find_user = ('SELECT * FROM user WHERE username = ?')
            conn.execute(find_user, [self.username.get()])
            if conn.fetchall():
                msg.showerror('Error','username already taken')
            else:
                msg.showinfo('Success!','Account Created Succesfully')
                self.log()
            # Create new account
            insert = 'INSERT INTO user(username, password) VALUES(?,?)'
            conn.commit()
            
            # Frame Packing Methods