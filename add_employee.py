import sqlite3
from tkinter import *

root = Tk()
root.title('Add Employee')
root.geometry('500x500')

conn = sqlite3.connect('company.db')
c = conn.cursor()

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

def query():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM employees")
    employees = c.fetchall()
    print(employees)
    print_employees = ''
    for employee in employees:
        print_employees += str(employee) + "/n"
    query_label = Label(root, text=print_employees)
    query_label.grid(row=4, column=0, columnspan=2)
    conn.commit()
    conn.close()

ID = Entry(root, width=30)
ID.grid(row=0, column=1, padx=20)
Name = Entry(root, width=30)
Name.grid(row=1, column=1)
DOB = Entry(root, width=30)
DOB.grid(row=2, column=1)
Gender = Entry(root, width=30)
Gender.grid(row=3, column=1)
Department = Entry(root, width=30)
Department.grid(row=4, column=1)
Position = Entry(root, width=30)
Position.grid(row=5, column=1)
Phone_Number = Entry(root, width=30)
Phone_Number.grid(row=6, column=1)
Email = Entry(root, width=30)
Email.grid(row=7, column=1)
Bank_Account = Entry(root, width=30)
Bank_Account.grid(row=8, column=1)
Social_Security_Number = Entry(root, width=30)
Social_Security_Number.grid(row=9, column=1)
Year_Joined = Entry(root, width=30)
Year_Joined.grid(row=10, column=1)
DepartmentID = Entry(root, width=30)
DepartmentID.grid(row=11, column=1)

ID_label = Label(root, text="ID")
ID_label.grid(row=0, column=0)
Name_label = Label(root, text="Name")
Name_label.grid(row=1, column=0)
DOB_label = Label(root, text="Date of Birth")
DOB_label.grid(row=2, column=0)
Gender_label = Label(root, text="Gender")
Gender_label.grid(row=3, column=0)
Department_label = Label(root, text="Department")
Department_label.grid(row=4, column=0)
Position_label = Label(root, text="Position")
Position_label.grid(row=5, column=0)
Phone_Number_label = Label(root, text="Phone Number")
Phone_Number_label.grid(row=6, column=0)
Email_label = Label(root, text="Email")
Email_label.grid(row=7, column=0)
Bank_Account_label = Label(root, text="Bank Account")
Bank_Account_label.grid(row=8, column=0)
Social_Security_Number_label = Label(root, text="Social Security Number")
Social_Security_Number_label.grid(row=9, column=0)
Year_Joined_label = Label(root, text="Year Joined")
Year_Joined_label.grid(row=10, column=0)
DepartmentID_label = Label(root, text="Department ID")
DepartmentID_label.grid(row=11, column=0)

enter_btn = Button(root, text="Add Employee To Database", command=enter)
enter_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Employees", commmand=query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

conn.commit()
conn.close()

root.mainloop()
