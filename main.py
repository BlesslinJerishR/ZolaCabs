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
            with sqlite3.connect('Users.db') as db:
                conn = db.cursor()
                
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
            with sqlite3.connect('User.db') as db:
                conn = db.cursor()
                
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
            db.commit()
            
        # Frame Packing Methods
        def log(self):
            self.username.set('')
            self.password.set('')
            self.crf.pack_forget()
            self.head['text'] = 'Login'
            self.logf.pack()
        
        def cr(self):
            self.new_user.set('')
            self.new_password.set('')
            self.logf.pack_forget()
            self.head['text'] = 'Register'
            self.crf.pack()
            
        # draw widgets
        def widgets(self):
            self.head = Label(self.master, text = "Login Panel", font=('open sans', 30), pady = 10)
            self.head.pack()
            self.logf = Frame(self.master, padx = 10, pady = 10)
            Label(self.logf, text = "Username : ", font = ('', 20), pady = 5, padx = 5).grid(sticky = W)
            Entry(self.logf, textvariable = self.username, bd = 5, font = ('', 15)).grid(row = 0, column = 1)
            Label(self.logf, text = "Password : ", font = ('', 20), pady = 5, padx = 5).grid(sticky = W)
            Entry(self.logf, textvariable = self.username, bd = 5, font = ('', 15), show='*').grid(row = 1, column = 1)
            Button(self.logf, text = " Login ", bd = 3, font = ('', 15), padx = 5, pady = 5, command = self.login).grid()