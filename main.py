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
home = tk.Frame(container)
add_department = tk.Frame(container)
add_employee = tk.Frame(container)
add_record = tk.Frame(container)

for F in (first, add_department, add_employee, add_record):
    F.grid(row=0, column=0, sticky="nsew")


def show_frame(frame_to_raise):
    frame_to_raise.tkraise()

# Code for first
Username = tk.Entry(first, width=30)
Username.grid(row=0, column=1, padx=20)
Passcode = tk.Entry(first, width=30)
Passcode.grid(row=1, column=1)

Username_label = tk.Label(first, text="Username", font=LARGE_FONT)
Username_label.grid(row=0, column=0)
Passcode_label = tk.Label(first, text="Passcode", font=LARGE_FONT)
Passcode_label.grid(row=1, column=0)

# Code for home
add_department_frame_btn = tk.Button(home, text="Add Department", command=lambda: show_frame(add_department))
add_department_frame_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



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

DepartmentID = tk.Entry(add_department, width=30)
DepartmentID.grid(row=0, column=1, padx=20)
Name = tk.Entry(add_department, width=30)
Name.grid(row=1, column=1)

DepartmentID_label = tk.Label(add_department, text="Department ID", font=LARGE_FONT)
DepartmentID_label.grid(row=0, column=0)
Name_label = tk.Label(root, text="Name", font=LARGE_FONT)
Name_label.grid(row=1, column=0)

add_department_btn = tk.Button(add_department, text="Add Department To Database", command=enter)
add_department_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Code for add_employee



show_frame(first)
root.mainloop()

