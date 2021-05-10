import sqlite3
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title('Company Database')

conn = sqlite3.connect('company.db')
c = conn.cursor()







conn.commit()
conn.close()
root.mainloop()
