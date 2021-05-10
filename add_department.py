import sqlite3
from tkinter import *

root = Tk()
root.title('Add Department')
root.geometry('500x500')

conn = sqlite3.connect('company.db')
c = conn.cursor()

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

def query():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM departments")
    departments = c.fetchall()
    print(departments)
    print_departments = ''
    for department in departments:
        print_departments += str(department) + "/n"
    query_label = Label(root, text=print_departments)
    query_label.grid(row=4, column=0, columnspan=2)
    conn.commit()
    conn.close()

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

query_btn = Button(root, text="Show Departments", commmand=query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

conn.commit()
conn.close()

root.mainloop()
