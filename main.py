import random
import time
import datetime
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

Item4 = 0

# Create a new DB if dir is 404 @startup

with sqlite3.connect('Users.db') as db:
    c = db.cursor()
    
c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT not NULL, password TEXT not NULL')
db.commit()
db.close()

