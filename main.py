import sqlite3
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

LARGE_FONT = ("Verdana", 12)
root = tk.Tk()
root.title('Company Database')
root.geometry('1000x621')
container = tk.Frame(root)

conn = sqlite3.connect('company.db')
c = conn.cursor()

container.pack(side="top", fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

first = tk.Frame(container)
home = tk.Frame(container)
department = tk.Frame(container)
employee = tk.Frame(container)
record = tk.Frame(container)

for F in (first, home, department, employee, record):
    F.grid(row=0, column=0, sticky="nsew")

def show_frame(frame_to_raise):
    frame_to_raise.tkraise()

# Code for first
def cancel_command():
    root.destroy()
    sys.exit()

def enter_command():
    if Username.get() == "Brent" and Passcode.get() == "1234":
        show_frame(home)
        Passcode.delete(0, END)
    else:
        mb.showerror("Error", "Incorrect Username or Passcode")
        Username.delete(0, END)
        Passcode.delete(0, END)

Username = tk.Entry(first, width=30)
Username.grid(row=0, column=1, padx=20)
Passcode = tk.Entry(first, width=30, show="•")
Passcode.grid(row=1, column=1)

Username_label = tk.Label(first, text="Username", font=LARGE_FONT)
Username_label.grid(row=0, column=0)
Passcode_label = tk.Label(first, text="Passcode", font=LARGE_FONT)
Passcode_label.grid(row=1, column=0)

home_btn = tk.Button(first, text="Enter", command=lambda: enter_command())
home_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

cancel_from_first_btn = tk.Button(first, text="Cancel", command=lambda: cancel_command())
cancel_from_first_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Code for home
department_btn = tk.Button(home, text="Database", command=lambda: show_frame(department))
department_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

cancel_from_home_btn = tk.Button(home, text="Cancel", command=lambda: show_frame(first))
cancel_from_home_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Code for department
tree = ttk.Treeview(department)
tree['columns'] = ("DepartmentID", "Name")

tree.column("#0", width=0, stretch=NO)
tree.column("DepartmentID", anchor=CENTER, width=120)
tree.column("Name", anchor=W, width=80)

tree.heading("#0", text="", anchor=W)
tree.heading("DepartmentID", text="Department ID", anchor=CENTER)
tree.heading("Name", text="Name", anchor=W)

tree.grid(row=0, column=0, pady=10, padx=260, ipadx=138)

def query_department_table():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM departments")
    items = c.fetchall()
    count = 0
    for department in items:
        tree.insert(parent='', index='end', iid=count, text="", values=(department[0], department[1]))
        count += 1
    conn.commit()
    conn.close()

def open_employee(e):
    show_frame(employee)

def select_department(e):
    tree_department_DepartmentID.delete(0, END)
    tree_department_Name.delete(0, END)

    selected = tree.focus()
    values = tree.item(selected, 'values')

    tree_department_DepartmentID.insert(0, values[0])
    tree_department_Name.insert(0, values[1])

def clear_department_entries():
    tree_department_DepartmentID.delete(0, END)
    tree_department_Name.delete(0, END)

def add_department():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("INSERT INTO departments VALUES (:Name)",
              {
                  'Name': tree_department_Name.get(),
              })

    conn.commit()
    conn.close()

    tree_department_DepartmentID.delete(0, END)
    tree_department_Name.delete(0, END)

    tree.delete(*tree.get_children())

    query_department_table()

def update_department():
    selected = tree.focus()
    tree.item(selected, text="", values=(tree_department_DepartmentID.get(), tree_department_Name.get()))

    conn = sqlite3.connect('company.db')

    c = conn.cursor()

    c.execute("""UPDATE departments SET
        Name = :Name
        WHERE oid = :oid""",
        {
            'Name': tree_department_Name.get(),
            'oid': tree_department_DepartmentID.get(),
        })

    conn.commit()
    conn.close()

    tree_department_DepartmentID.delete(0, END)
    tree_department_Name.delete(0, END)

def delete_department():
    a = tree.selection()[0]
    tree.delete(a)

    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    c.execute("DELETE FROM departments WHERE oid= :oid",
              {
                  'Name': tree_department_Name.get(),
                  'oid': tree_department_DepartmentID.get(),
              })

    conn.commit()
    conn.close()

    tree_department_DepartmentID.delete(0, END)
    tree_department_Name.delete(0, END)

def department_up():
    lines = tree.selection()
    for line in lines:
        tree.move(line, tree.parent(line), tree.index(line) - 1)

def department_down():
    lines = tree.selection()
    for line in reversed(lines):
        tree.move(line, tree.parent(line), tree.index(line) + 1)

tree_department_frame = Frame(department)
tree_department_frame.grid(row=1, column=0)

tree_department_DepartmentID_label = tk.Label(tree_department_frame, text="Department ID")
tree_department_DepartmentID_label.grid(row=2, column=0)

tree_department_Name_label = tk.Label(tree_department_frame, text="Name")
tree_department_Name_label.grid(row=2, column=1)

tree_department_DepartmentID = tk.Entry(tree_department_frame)
tree_department_DepartmentID.grid(row=3, column=0)

tree_department_Name = tk.Entry(tree_department_frame)
tree_department_Name.grid(row=3, column=1)

clear_department_entries_btn = tk.Button(department, text="Clear Entries", command=clear_department_entries)
clear_department_entries_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

add_department_btn = tk.Button(department, text="Add Department", command=add_department)
add_department_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

update_department_btn = tk.Button(department, text="Update Department", command=update_department)
update_department_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

delete_department_btn = tk.Button(department, text="Delete Department", command=delete_department)
delete_department_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

department_up_btn = tk.Button(department, text="↑", command=department_up)
department_up_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

department_down_btn = tk.Button(department, text="↓", command=department_down)
department_down_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

cancel_from_department_btn = tk.Button(department, text="Cancel", command=lambda: show_frame(home))
cancel_from_department_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

tree.bind("<ButtonRelease-1>", select_department)
tree.bind("<Return>", open_employee)

# Code for employee
tree2 = ttk.Treeview(employee)
tree2.pack(pady=10, padx=10)
tree2['columns'] = ("ID", "Name", "DOB", "Gender", "Department", "Position", "Phone_Number", "Email", "Account", "Account_Number", "Social_Security_Number", "Joined")

tree2.column("#0", width=0, stretch=NO)
tree2.column("ID", anchor=CENTER, width=180)
tree2.column("Name", anchor=W, width=180)
tree2.column("DOB", anchor=W, width=180)
tree2.column("Gender", anchor=W, width=180)
tree2.column("Department", anchor=W, width=180)
tree2.column("Position", anchor=W, width=180)
tree2.column("Phone_Number", anchor=W, width=180)
tree2.column("Email", anchor=W, width=180)
tree2.column("Account", anchor=W, width=180)
tree2.column("Account_Number", anchor=W, width=180)
tree2.column("Social_Security_Number", anchor=W, width=180)
tree2.column("Joined", anchor=W, width=180)

tree2.heading("#0", text="", anchor=W)
tree2.heading("ID", text="ID", anchor=CENTER)
tree2.heading("Name", text="Name", anchor=W)
tree2.heading("DOB", text="DOB", anchor=W)
tree2.heading("Gender", text="Gender", anchor=W)
tree2.heading("Department", text="Department", anchor=W)
tree2.heading("Position", text="Position", anchor=W)
tree2.heading("Phone_Number", text="Phone", anchor=W)
tree2.heading("Email", text="Email", anchor=W)
tree2.heading("Account", text="Account", anchor=W)
tree2.heading("Account_Number", text="Account No", anchor=W)
tree2.heading("Social_Security_Number", text="SSS", anchor=W)
tree2.heading("Joined", text="Joined", anchor=W)

def query_employee_table():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM employees")
    items = c.fetchall()
    count = 0
    for employee in items:
        tree2.insert(parent='', index='end', iid=count, text="", values=(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5], employee[6], employee[7], employee[8], employee[9], employee[10], employee[11]))
        count += 1
    conn.commit()
    conn.close()

def open_record(e):
    show_frame(record)

def select_employee(e):
    tree_employee_ID.delete(0, END)
    tree_employee_Name.delete(0, END)
    tree_employee_DOB.delete(0, END)
    tree_employee_Gender.delete(0, END)
    tree_employee_Department.delete(0, END)
    tree_employee_Position.delete(0, END)
    tree_employee_Phone_Number.delete(0, END)
    tree_employee_Email.delete(0, END)
    tree_employee_Account.delete(0, END)
    tree_employee_Account_Number.delete(0, END)
    tree_employee_Social_Security_Number.delete(0, END)
    tree_employee_Joined.delete(0, END)

    selected = tree2.focus()
    values = tree2.item(selected, 'values')

    tree_employee_ID.insert(0, values[0])
    tree_employee_Name.insert(0, values[1])
    tree_employee_DOB.insert(0, values[2])
    tree_employee_Gender.insert(0, values[3])
    tree_employee_Department.insert(0, values[4])
    tree_employee_Position.insert(0, values[5])
    tree_employee_Phone_Number.insert(0, values[6])
    tree_employee_Email.insert(0, values[7])
    tree_employee_Account.insert(0, values[8])
    tree_employee_Account_Number.insert(0, values[9])
    tree_employee_Social_Security_Number.insert(0, values[10])
    tree_employee_Joined.insert(0, values[11])

def clear_employee_entries():
    tree_employee_ID.delete(0, END)
    tree_employee_Name.delete(0, END)
    tree_employee_DOB.delete(0, END)
    tree_employee_Gender.delete(0, END)
    tree_employee_Department.delete(0, END)
    tree_employee_Position.delete(0, END)
    tree_employee_Phone_Number.delete(0, END)
    tree_employee_Email.delete(0, END)
    tree_employee_Account.delete(0, END)
    tree_employee_Account_Number.delete(0, END)
    tree_employee_Social_Security_Number.delete(0, END)
    tree_employee_Joined.delete(0, END)

def add_employee():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees VALUES (:Name, :DOB, :Gender, :Department, :Position, :Phone_Number, :Email, :Account, :Account_Number, :Social_Security_Number, :Joined)",
              {
                  'Name': tree_employee_Name.get(),
                  'DOB': tree_employee_DOB.get(),
                  'Gender': tree_employee_Gender.get(),
                  'Department': tree_employee_Department.get(),
                  'Position': tree_employee_Position.get(),
                  'Phone_Number': tree_employee_Phone_Number.get(),
                  'Email': tree_employee_Email.get(),
                  'Account': tree_employee_Account.get(),
                  'Account_Number': tree_employee_Account_Number.get(),
                  'Social_Security_Number': tree_employee_Social_Security_Number.get(),
                  'Joined': tree_employee_Joined.get(),
              })

    conn.commit()
    conn.close()

    tree_employee_ID.delete(0, END)
    tree_employee_Name.delete(0, END)
    tree_employee_DOB.delete(0, END)
    tree_employee_Gender.delete(0, END)
    tree_employee_Department.delete(0, END)
    tree_employee_Position.delete(0, END)
    tree_employee_Phone_Number.delete(0, END)
    tree_employee_Email.delete(0, END)
    tree_employee_Account.delete(0, END)
    tree_employee_Account_Number.delete(0, END)
    tree_employee_Social_Security_Number.delete(0, END)
    tree_employee_Joined.delete(0, END)

    tree2.delete(*tree2.get_children())

    query_employee_table()

def update_employee():
    selected = tree2.focus()
    tree2.item(selected, text="", values=(tree_employee_ID.get(), tree_employee_Name.get(), tree_employee_DOB.get(), tree_employee_Gender.get(), tree_employee_Department.get(), tree_employee_Position.get(), tree_employee_Phone_Number.get(), tree_employee_Email.get(), tree_employee_Account.get(), tree_employee_Account_Number.get(), tree_employee_Social_Security_Number.get(), tree_employee_Joined.get()))

    conn = sqlite3.connect('company.db')

    c = conn.cursor()

    c.execute("""UPDATE employees SET
        Name = :Name,
        DOB = :DOB,
        Gender = :Gender,
        Department = :Department,
        Position = :Position,
        Phone_Number = :Phone_Number,
        Email = :Email,
        Account = :Account,
        Account_Number = :Account_Number,
        Social_Security_Number = :Social_Security_Number,
        Joined = :Joined
        WHERE oid = :oid""",
        {
            'Name': tree_employee_Name.get(),
            'DOB': tree_employee_DOB.get(),
            'Gender': tree_employee_Gender.get(),
            'Department': tree_employee_Department.get(),
            'Position': tree_employee_Position.get(),
            'Phone_Number': tree_employee_Phone_Number.get(),
            'Email': tree_employee_Email.get(),
            'Account': tree_employee_Account.get(),
            'Account_Number': tree_employee_Account_Number.get(),
            'Social_Security_Number': tree_employee_Social_Security_Number.get(),
            'Joined': tree_employee_Joined.get(),
            'oid': tree_employee_ID.get(),
        })

    conn.commit()
    conn.close()

    tree_employee_ID.delete(0, END)
    tree_employee_Name.delete(0, END)
    tree_employee_DOB.delete(0, END)
    tree_employee_Gender.delete(0, END)
    tree_employee_Department.delete(0, END)
    tree_employee_Position.delete(0, END)
    tree_employee_Phone_Number.delete(0, END)
    tree_employee_Email.delete(0, END)
    tree_employee_Account.delete(0, END)
    tree_employee_Account_Number.delete(0, END)
    tree_employee_Social_Security_Number.delete(0, END)
    tree_employee_Joined.delete(0, END)

def delete_employee():
    a = tree2.selection()[0]
    tree2.delete(a)

    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    c.execute("DELETE FROM employees WHERE oid= :oid",
              {
                  'Name': tree_employee_Name.get(),
                  'DOB': tree_employee_DOB.get(),
                  'Gender': tree_employee_Gender.get(),
                  'Department': tree_employee_Department.get(),
                  'Position': tree_employee_Position.get(),
                  'Phone_Number': tree_employee_Phone_Number.get(),
                  'Email': tree_employee_Email.get(),
                  'Account': tree_employee_Account.get(),
                  'Account_Number': tree_employee_Account_Number.get(),
                  'Social_Security_Number': tree_employee_Social_Security_Number.get(),
                  'Joined': tree_employee_Joined.get(),
                  'oid': tree_employee_ID.get(),
              })

    conn.commit()
    conn.close()

    tree_employee_ID.delete(0, END)
    tree_employee_Name.delete(0, END)
    tree_employee_DOB.delete(0, END)
    tree_employee_Gender.delete(0, END)
    tree_employee_Department.delete(0, END)
    tree_employee_Position.delete(0, END)
    tree_employee_Phone_Number.delete(0, END)
    tree_employee_Email.delete(0, END)
    tree_employee_Account.delete(0, END)
    tree_employee_Account_Number.delete(0, END)
    tree_employee_Social_Security_Number.delete(0, END)
    tree_employee_Joined.delete(0, END)

def employee_up():
    lines = tree2.selection()
    for line in lines:
        tree2.move(line, tree2.parent(line), tree2.index(line) - 1)

def employee_down():
    lines = tree2.selection()
    for line in reversed(lines):
        tree2.move(line, tree2.parent(line), tree2.index(line) + 1)

tree_employee_frame = tk.Frame(employee)
tree_employee_frame.pack(fill="y", expand="yes")

tree_employee_ID_label = tk.Label(tree_employee_frame, text="ID")
tree_employee_ID_label.grid(row=0, column=0)

tree_employee_Name_label = tk.Label(tree_employee_frame, text="Name")
tree_employee_Name_label.grid(row=0, column=1)

tree_employee_DOB_label = tk.Label(tree_employee_frame, text="DOB")
tree_employee_DOB_label.grid(row=0, column=2)

tree_employee_Gender_label = tk.Label(tree_employee_frame, text="Gender")
tree_employee_Gender_label.grid(row=0, column=3)

tree_employee_Department_label = tk.Label(tree_employee_frame, text="Department")
tree_employee_Department_label.grid(row=0, column=4)

tree_employee_Position_label = tk.Label(tree_employee_frame, text="Position")
tree_employee_Position_label.grid(row=2, column=0)

tree_employee_Phone_Number_label = tk.Label(tree_employee_frame, text="Phone")
tree_employee_Phone_Number_label.grid(row=2, column=1)

tree_employee_Email_label = tk.Label(tree_employee_frame, text="Email")
tree_employee_Email_label.grid(row=2, column=2)

tree_employee_Account_label = tk.Label(tree_employee_frame, text="Account")
tree_employee_Account_label.grid(row=2, column=3)

tree_employee_Account_Number_label = tk.Label(tree_employee_frame, text="Account No")
tree_employee_Account_Number_label.grid(row=2, column=4)

tree_employee_Social_Security_Number_label = tk.Label(tree_employee_frame, text="SSS")
tree_employee_Social_Security_Number_label.grid(row=4, column=0)

tree_employee_Joined_label = tk.Label(tree_employee_frame, text="Joined")
tree_employee_Joined_label.grid(row=4, column=1)

tree_employee_ID = tk.Entry(tree_employee_frame)
tree_employee_ID.grid(row=1, column=0)

tree_employee_Name = tk.Entry(tree_employee_frame)
tree_employee_Name.grid(row=1, column=1)

tree_employee_DOB = tk.Entry(tree_employee_frame)
tree_employee_DOB.grid(row=1, column=2)

tree_employee_Gender = tk.Entry(tree_employee_frame)
tree_employee_Gender.grid(row=1, column=3)

tree_employee_Department = tk.Entry(tree_employee_frame)
tree_employee_Department.grid(row=1, column=4)

tree_employee_Position = tk.Entry(tree_employee_frame)
tree_employee_Position.grid(row=3, column=0)

tree_employee_Phone_Number = tk.Entry(tree_employee_frame)
tree_employee_Phone_Number.grid(row=3, column=1)

tree_employee_Email = tk.Entry(tree_employee_frame)
tree_employee_Email.grid(row=3, column=2)

tree_employee_Account = tk.Entry(tree_employee_frame)
tree_employee_Account.grid(row=3, column=3)

tree_employee_Account_Number = tk.Entry(tree_employee_frame)
tree_employee_Account_Number.grid(row=3, column=4)

tree_employee_Social_Security_Number = tk.Entry(tree_employee_frame)
tree_employee_Social_Security_Number.grid(row=5, column=0)

tree_employee_Joined = tk.Entry(tree_employee_frame)
tree_employee_Joined.grid(row=5, column=1)

clear_employee_entries_btn = tk.Button(tree_employee_frame, text="Clear Entries", command=clear_employee_entries)
clear_employee_entries_btn.grid(row=6, column=0, columnspan=3, pady=10, padx=10, ipadx=102)

add_employee_btn = tk.Button(tree_employee_frame, text="Add Employee", command=add_employee)
add_employee_btn.grid(row=6, column=2, columnspan=3, pady=10, padx=10, ipadx=98)

update_employee_btn = tk.Button(tree_employee_frame, text="Update Employee", command=update_employee)
update_employee_btn.grid(row=7, column=0, columnspan=3, pady=10, padx=10, ipadx=98)

delete_employee_btn = tk.Button(tree_employee_frame, text="Delete Employee", command=delete_employee)
delete_employee_btn.grid(row=7, column=2, columnspan=3, pady=10, padx=10, ipadx=100)

employee_up_btn = tk.Button(tree_employee_frame, text="↑", command=employee_up)
employee_up_btn.grid(row=8, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

employee_down_btn = tk.Button(tree_employee_frame, text="↓", command=employee_down)
employee_down_btn.grid(row=8, column=2, columnspan=3, pady=10, padx=10, ipadx=100)

cancel_from_employee_btn = tk.Button(tree_employee_frame, text="Cancel", command=lambda: show_frame(home))
cancel_from_employee_btn.grid(row=9, column=1, columnspan=3, pady=10, padx=100, ipadx=150)

tree2.bind("<ButtonRelease-1>", select_employee)
tree2.bind("<Return>", open_record)

# Code for record
tree3 = ttk.Treeview(record)
tree3.pack(pady=10, padx=10)
tree3['columns'] = ("ID", "Name", "Record_Date_M", "Record_Date_D", "Record_Date_Y", "Time_In_Hour", "Time_In_Minute", "Time_Out_Hour", "Time_Out_Minute")

tree3.column("#0", width=0, stretch=NO)
tree3.column("ID", anchor=CENTER, width=180)
tree3.column("Name", anchor=W, width=180)
tree3.column("Record_Date_M", anchor=W, width=180)
tree3.column("Record_Date_D", anchor=W, width=180)
tree3.column("Record_Date_Y", anchor=W, width=180)
tree3.column("Time_In_Hour", anchor=W, width=180)
tree3.column("Time_In_Minute", anchor=W, width=180)
tree3.column("Time_Out_Hour", anchor=W, width=180)
tree3.column("Time_Out_Minute", anchor=W, width=180)

tree3.heading("#0", text="", anchor=W)
tree3.heading("ID", text="ID", anchor=CENTER)
tree3.heading("Name", text="Name", anchor=W)
tree3.heading("Record_Date_M", text="Month", anchor=W)
tree3.heading("Record_Date_D", text="Day", anchor=W)
tree3.heading("Record_Date_Y", text="Year", anchor=W)
tree3.heading("Time_In_Hour", text="Time In Hour", anchor=W)
tree3.heading("Time_In_Minute", text="Time In Minute", anchor=W)
tree3.heading("Time_Out_Hour", text="Time Out Hour", anchor=W)
tree3.heading("Time_Out_Minute", text="Time Out Minute", anchor=W)

def query_record_table():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM records")
    items = c.fetchall()
    count = 0
    for record in items:
        tree3.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]))
        count += 1
    conn.commit()
    conn.close()

def select_record(e):
    tree_record_ID.delete(0, END)
    tree_record_Name.delete(0, END)
    tree_record_Record_Date_M.delete(0, END)
    tree_record_Record_Date_D.delete(0, END)
    tree_record_Record_Date_Y.delete(0, END)
    tree_record_Time_In_Hour.delete(0, END)
    tree_record_Time_In_Minute.delete(0, END)
    tree_record_Time_Out_Hour.delete(0, END)
    tree_record_Time_Out_Minute.delete(0, END)

    selected = tree3.focus()
    values = tree3.item(selected, 'values')

    tree_record_ID.insert(0, values[0])
    tree_record_Name.insert(0, values[1])
    tree_record_Record_Date_M.insert(0, values[2])
    tree_record_Record_Date_D.insert(0, values[3])
    tree_record_Record_Date_Y.insert(0, values[4])
    tree_record_Time_In_Hour.insert(0, values[5])
    tree_record_Time_In_Minute.insert(0, values[6])
    tree_record_Time_Out_Hour.insert(0, values[7])
    tree_record_Time_Out_Minute.insert(0, values[8])

def clear_record_entries():
    tree_record_ID.delete(0, END)
    tree_record_Name.delete(0, END)
    tree_record_Record_Date_M.delete(0, END)
    tree_record_Record_Date_D.delete(0, END)
    tree_record_Record_Date_Y.delete(0, END)
    tree_record_Time_In_Hour.delete(0, END)
    tree_record_Time_In_Minute.delete(0, END)
    tree_record_Time_Out_Hour.delete(0, END)
    tree_record_Time_Out_Minute.delete(0, END)

def add_record():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("INSERT INTO records VALUES (:Name, :Record_Date_M, :Record_Date_D, :Record_Date_Y, :Time_In_Hour, :Time_In_Minute, :Time_Out_Hour, :Time_Out_Minute)",
              {
                  'Name': tree_record_Name.get(),
                  'Record_Date_M': tree_record_Record_Date_M.get(),
                  'Record_Date_D': tree_record_Record_Date_D.get(),
                  'Record_Date_Y': tree_record_Record_Date_Y.get(),
                  'Time_In_Hour': tree_record_Time_In_Hour.get(),
                  'Time_In_Minute': tree_record_Time_In_Minute.get(),
                  'Time_Out_Hour': tree_record_Time_Out_Hour.get(),
                  'Time_Out_Minute': tree_record_Time_Out_Minute.get(),
              })

    conn.commit()
    conn.close()

    tree_record_ID.delete(0, END)
    tree_record_Name.delete(0, END)
    tree_record_Record_Date_M.delete(0, END)
    tree_record_Record_Date_D.delete(0, END)
    tree_record_Record_Date_Y.delete(0, END)
    tree_record_Time_In_Hour.delete(0, END)
    tree_record_Time_In_Minute.delete(0, END)
    tree_record_Time_Out_Hour.delete(0, END)
    tree_record_Time_Out_Minute.delete(0, END)

    tree3.delete(*tree3.get_children())

    query_record_table()

def update_record():
    selected = tree3.focus()
    tree3.item(selected, text="", values=(tree_record_ID.get(), tree_record_Name.get(), tree_record_Record_Date_M.get(), tree_record_Record_Date_D.get(), tree_record_Record_Date_Y.get(), tree_record_Time_In_Hour.get(), tree_record_Time_In_Minute.get(), tree_record_Time_Out_Hour.get(), tree_record_Time_Out_Minute.get()))

    conn = sqlite3.connect('company.db')

    c = conn.cursor()

    c.execute("""UPDATE records SET
        Name = :Name,
        Record_Date_M = :Record_Date_M,
        Record_Date_D = :Record_Date_D,
        Record_Date_Y = :Record_Date_Y,
        Time_In_Hour = :Time_In_Hour,
        Time_In_Minute = :Time_In_Minute,
        Time_Out_Hour = :Time_Out_Hour,
        Time_Out_Minute = :Time_Out_Minute
        WHERE oid = :oid""",
        {
            'Name': tree_record_Name.get(),
            'Record_Date_M': tree_record_Record_Date_M.get(),
            'Record_Date_D': tree_record_Record_Date_D.get(),
            'Record_Date_Y': tree_record_Record_Date_Y.get(),
            'Time_In_Hour': tree_record_Time_In_Hour.get(),
            'Time_In_Minute': tree_record_Time_In_Minute.get(),
            'Time_Out_Hour': tree_record_Time_Out_Hour.get(),
            'Time_Out_Minute': tree_record_Time_Out_Minute.get(),
            'oid': tree_record_ID.get(),
        })

    conn.commit()
    conn.close()

    tree_record_ID.delete(0, END)
    tree_record_Name.delete(0, END)
    tree_record_Record_Date_M.delete(0, END)
    tree_record_Record_Date_D.delete(0, END)
    tree_record_Record_Date_Y.delete(0, END)
    tree_record_Time_In_Hour.delete(0, END)
    tree_record_Time_In_Minute.delete(0, END)
    tree_record_Time_Out_Hour.delete(0, END)
    tree_record_Time_Out_Minute.delete(0, END)

def delete_record():
    a = tree3.selection()[0]
    tree3.delete(a)

    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    c.execute("DELETE FROM records WHERE oid= :oid",
              {
                  'Name': tree_record_Name.get(),
                  'Record_Date_M': tree_record_Record_Date_M.get(),
                  'Record_Date_D': tree_record_Record_Date_D.get(),
                  'Record_Date_Y': tree_record_Record_Date_Y.get(),
                  'Time_In_Hour': tree_record_Time_In_Hour.get(),
                  'Time_In_Minute': tree_record_Time_In_Minute.get(),
                  'Time_Out_Hour': tree_record_Time_Out_Hour.get(),
                  'Time_Out_Minute': tree_record_Time_Out_Minute.get(),
                  'oid': tree_record_ID.get(),
              })

    conn.commit()
    conn.close()

    tree_record_ID.delete(0, END)
    tree_record_Name.delete(0, END)
    tree_record_Record_Date_M.delete(0, END)
    tree_record_Record_Date_D.delete(0, END)
    tree_record_Record_Date_Y.delete(0, END)
    tree_record_Time_In_Hour.delete(0, END)
    tree_record_Time_In_Minute.delete(0, END)
    tree_record_Time_Out_Hour.delete(0, END)
    tree_record_Time_Out_Minute.delete(0, END)

def record_up():
    lines = tree3.selection()
    for line in lines:
        tree3.move(line, tree3.parent(line), tree3.index(line) - 1)

def record_down():
    lines = tree3.selection()
    for line in reversed(lines):
        tree3.move(line, tree3.parent(line), tree3.index(line) + 1)

tree_record_frame = tk.Frame(record)
tree_record_frame.pack(fill="y", expand="yes")

tree_record_ID_label = tk.Label(tree_record_frame, text="ID")
tree_record_ID_label.grid(row=0, column=0)

tree_record_Name_label = tk.Label(tree_record_frame, text="Name")
tree_record_Name_label.grid(row=0, column=1)

tree_record_Record_Date_M_label = tk.Label(tree_record_frame, text="Month")
tree_record_Record_Date_M_label.grid(row=0, column=2)

tree_record_Record_Date_D_label = tk.Label(tree_record_frame, text="Day")
tree_record_Record_Date_D_label.grid(row=0, column=3)

tree_record_Record_Date_Y_label = tk.Label(tree_record_frame, text="Year")
tree_record_Record_Date_Y_label.grid(row=0, column=4)

tree_record_Time_In_Hour_label = tk.Label(tree_record_frame, text="Time In Hour")
tree_record_Time_In_Hour_label.grid(row=2, column=0)

tree_record_Time_In_Minute_label = tk.Label(tree_record_frame, text="Time In Minute")
tree_record_Time_In_Minute_label.grid(row=2, column=1)

tree_record_Time_Out_Hour_label = tk.Label(tree_record_frame, text="Time Out Hour")
tree_record_Time_Out_Hour_label.grid(row=2, column=2)

tree_record_Time_Out_Minute_label = tk.Label(tree_record_frame, text="Time Out Minute")
tree_record_Time_Out_Minute_label.grid(row=2, column=3)

tree_record_ID = tk.Entry(tree_record_frame)
tree_record_ID.grid(row=1, column=0)

tree_record_Name = tk.Entry(tree_record_frame)
tree_record_Name.grid(row=1, column=1)

tree_record_Record_Date_M = tk.Entry(tree_record_frame)
tree_record_Record_Date_M.grid(row=1, column=2)

tree_record_Record_Date_D = tk.Entry(tree_record_frame)
tree_record_Record_Date_D.grid(row=1, column=3)

tree_record_Record_Date_Y = tk.Entry(tree_record_frame)
tree_record_Record_Date_Y.grid(row=1, column=4)

tree_record_Time_In_Hour = tk.Entry(tree_record_frame)
tree_record_Time_In_Hour.grid(row=3, column=0)

tree_record_Time_In_Minute = tk.Entry(tree_record_frame)
tree_record_Time_In_Minute.grid(row=3, column=1)

tree_record_Time_Out_Hour = tk.Entry(tree_record_frame)
tree_record_Time_Out_Hour.grid(row=3, column=2)

tree_record_Time_Out_Minute = tk.Entry(tree_record_frame)
tree_record_Time_Out_Minute.grid(row=3, column=3)

clear_record_entries_btn = tk.Button(tree_record_frame, text="Clear Entries", command=clear_record_entries)
clear_record_entries_btn.grid(row=4, column=0, columnspan=3, pady=10, padx=10, ipadx=102)

add_record_btn = tk.Button(tree_record_frame, text="Add Record", command=add_record)
add_record_btn.grid(row=4, column=2, columnspan=3, pady=10, padx=10, ipadx=98)

update_record_btn = tk.Button(tree_record_frame, text="Update Record", command=update_record)
update_record_btn.grid(row=5, column=0, columnspan=3, pady=10, padx=10, ipadx=98)

delete_record_btn = tk.Button(tree_record_frame, text="Delete Record", command=delete_record)
delete_record_btn.grid(row=5, column=2, columnspan=3, pady=10, padx=10, ipadx=100)

record_up_btn = tk.Button(tree_record_frame, text="↑", command=record_up)
record_up_btn.grid(row=6, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

record_down_btn = tk.Button(tree_record_frame, text="↓", command=record_down)
record_down_btn.grid(row=6, column=2, columnspan=3, pady=10, padx=10, ipadx=100)

cancel_from_record_btn = tk.Button(tree_record_frame, text="Cancel", command=lambda: show_frame(home))
cancel_from_record_btn.grid(row=7, column=1, columnspan=3, pady=10, padx=100, ipadx=150)

tree3.bind("<ButtonRelease-1>", select_record)

show_frame(first)
query_department_table()
query_employee_table()
query_record_table()
root.mainloop()
