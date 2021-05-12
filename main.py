import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('company.db')
c = conn.cursor()

LARGE_FONT = ("Verdana", 12)
root = tk.Tk()
container = tk.Frame(root)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

login = tk.Frame(container)
add_department = tk.Frame(container)
add_employee = tk.Frame(container)
for F in (login, add_department, add_employee):
    F.grid(row=0, column=0, sticky="nsew")

def show_frame(frame_to_raise):
    frame_to_raise.tkraise()

# Code for add_department












root.mainloop()
