import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

LARGE_FONT = ("Verdana", 12)
root = tk.Tk()
container = tk.Frame(root)

container.pack(side="top", fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

first = tk.Frame(container)
add_department = tk.Frame(container)
add_employee = tk.Frame(container)
add_record = tk.Frame(container)

for F in (first, add_department, add_employee, add_record):
    F.grid(row=0, column=0, sticky="nsew")


def show_frame(frame_to_raise):
    frame_to_raise.tkraise()

# Code for first






show_frame(first)
root.mainloop()

