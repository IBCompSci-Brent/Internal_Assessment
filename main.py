import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

LARGE_FONT = ("Verdana", 12)
root = tk.Tk()
root.title('Company Database')
root.geometry('500x500')
container = tk.Frame(root)

conn = sqlite3.connect('company.db')
c = conn.cursor()

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

# Code for add_department
def enter():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("INSERT INTO departments VALUES (:DepartmentID, :Name)",
            {
                'DepartmentID': DepartmentID.get(),
                'Name': Name.get()
            })
    conn.commit()
    conn.close()
    DepartmentID.delete(0, END)
    Name.delete(0, END)

DepartmentID = Entry(root, width=30)
DepartmentID.grid(row=0, column=1, padx=20)
Name = Entry(root, width=30)
Name.grid(row=1, column=1)

DepartmentID_label = Label(root, text="Department ID")
DepartmentID_label.grid(row=0, column=0)
Name_label = Label(root, text="Name")
Name_label.grid(row=1, column=0)

enter_btn = Button(root, text="Add Department To Database", command=enter)
enter_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)






conn.commit()
conn.close()
show_frame(first)
root.mainloop()

