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
add_department_frame_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



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
Name_label = tk.Label(add_department, text="Name", font=LARGE_FONT)
Name_label.grid(row=1, column=0)

add_department_btn = tk.Button(add_department, text="Add Department To Database", command=enter)
add_department_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

back_to_home_from_add_department_btn = tk.Button(add_department, text="Back to Home", command=lambda: show_frame(home))
back_to_home_from_add_department_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Code for add_employee
def enter():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees VALUES (:ID, :Name, :DOB, :Gender, :Department, :Position, :Phone_Number, :Email, :Bank_Account, :Social_Security_Number, :Year_Joined, :DepartmentID)",
            {
                'ID': ID.get(),
                'Name': Name.get(),
                'DOB': DOB.get(),
                'Gender': Gender.get(),
                'Department': Department.get(),
                'Position': Position.get(),
                'Phone_Number': Phone_Number.get(),
                'Email': Email.get(),
                'Bank_Account': Bank_Account.get(),
                'Social_Security_Number': Social_Security_Number.get(),
                'Year_Joined': Year_Joined.get(),
                'DepartmentID': DepartmentID.get()
            })
    conn.commit()
    conn.close()
    ID.delete(0, END)
    Name.delete(0, END)
    DOB.delete(0, END)
    Gender.delete(0, END)
    Department.delete(0, END)
    Position.delete(0, END)
    Phone_Number.delete(0, END)
    Email.delete(0, END)
    Bank_Account.delete(0, END)
    Social_Security_Number.delete(0, END)
    Year_Joined.delete(0, END)
    DepartmentID.delete(0, END)

ID = tk.Entry(add_employee, width=30)
ID.grid(row=0, column=1, padx=20)
Name = tk.Entry(add_employee, width=30)
Name.grid(row=1, column=1)
DOB = tk.Entry(add_employee, width=30)
DOB.grid(row=2, column=1)
Gender = tk.Entry(add_employee, width=30)
Gender.grid(row=3, column=1)
Department = tk.Entry(add_employee, width=30)
Department.grid(row=4, column=1)
Position = tk.Entry(add_employee, width=30)
Position.grid(row=5, column=1)
Phone_Number = tk.Entry(add_employee, width=30)
Phone_Number.grid(row=6, column=1)
Email = tk.Entry(add_employee, width=30)
Email.grid(row=7, column=1)
Bank_Account = tk.Entry(add_employee, width=30)
Bank_Account.grid(row=8, column=1)
Social_Security_Number = tk.Entry(add_employee, width=30)
Social_Security_Number.grid(row=9, column=1)
Year_Joined = tk.Entry(add_employee, width=30)
Year_Joined.grid(row=10, column=1)
DepartmentID = tk.Entry(add_employee, width=30)
DepartmentID.grid(row=11, column=1)

ID_label = tk.Label(add_employee, text="ID", font=LARGE_FONT)
ID_label.grid(row=0, column=0)
Name_label = tk.Label(add_employee, text="Name", font=LARGE_FONT)
Name_label.grid(row=1, column=0)
DOB_label = Label(add_employee, text="Date of Birth", font=LARGE_FONT)
DOB_label.grid(row=2, column=0)
Gender_label = tk.Label(add_employee, text="Gender", font=LARGE_FONT)
Gender_label.grid(row=3, column=0)
Department_label = tk.Label(add_employee, text="Department", font=LARGE_FONT)
Department_label.grid(row=4, column=0)
Position_label = tk.Label(add_employee, text="Position", font=LARGE_FONT)
Position_label.grid(row=5, column=0)
Phone_Number_label = tk.Label(add_employee, text="Phone Number", font=LARGE_FONT)
Phone_Number_label.grid(row=6, column=0)
Email_label = tk.Label(add_employee, text="Email", font=LARGE_FONT)
Email_label.grid(row=7, column=0)
Bank_Account_label = tk.Label(add_employee, text="Bank Account", font=LARGE_FONT)
Bank_Account_label.grid(row=8, column=0)
Social_Security_Number_label = tk.Label(add_employee, text="Social Security Number", font=LARGE_FONT)
Social_Security_Number_label.grid(row=9, column=0)
Year_Joined_label = tk.Label(add_employee, text="Year Joined", font=LARGE_FONT)
Year_Joined_label.grid(row=10, column=0)
DepartmentID_label = tk.Label(add_employee, text="Department ID", font=LARGE_FONT)
DepartmentID_label.grid(row=11, column=0)

add_employee_btn = tk.Button(add_employee, text="Add Employee To Database", command=enter)
add_employee_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

back_to_home_from_add_employee_btn = tk.Button(add_employee, text="Back to Home", command=lambda: show_frame(home))
back_to_home_from_add_employee_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

show_frame(first)
root.mainloop()

