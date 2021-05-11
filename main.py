import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('company.db')
c = conn.cursor()


root = Tk()






conn.commit()
conn.close()
root.mainloop()
