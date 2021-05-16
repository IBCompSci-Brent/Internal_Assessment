import sqlite3
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

LARGE_FONT = ("Verdana", 12)
root = tk.Tk()
root.title('Company Database')
root.geometry('500x600')
container = tk.Frame(root)

conn = sqlite3.connect('company.db')
c = conn.cursor()

container.pack(side="top", fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

first = tk.Frame(container)
home = tk.Frame(container)
department = tk.Frame(container)

for F in (first, home, department):
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

# Code for database
tree = ttk.Treeview(department)
tree['columns'] = ("DepartmentID", "Name")

tree.column("#0", width=0, stretch=NO)
tree.column("DepartmentID", anchor=CENTER, width=120)
tree.column("Name", anchor=W, width=80)

tree.heading("#0", text="", anchor=W)
tree.heading("DepartmentID", text="Department ID", anchor=CENTER)
tree.heading("Name", text="Name", anchor=W)

tree.grid(row=0, column=0, pady=10, padx=10, ipadx=138)

def query_database():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM departments")
    items = c.fetchall()
    global count
    count = 0
    for department in items:
        tree.insert(parent='', index='end', iid=count, text="", values=(department[0], department[1]))
        count += 1
    conn.commit()
    conn.close()

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

    query_database()

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

def up():
    lines = tree.selection()
    for line in lines:
        tree.move(line, tree.parent(line), tree.index(line) - 1)

def down():
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

department_up_btn = tk.Button(department, text="↑", command=up)
department_up_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

department_down_btn = tk.Button(department, text="↓", command=down)
department_down_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

cancel_from_department_btn = tk.Button(department, text="Cancel", command=lambda: show_frame(home))
cancel_from_department_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

tree.bind("<ButtonRelease-1>", select_department)


show_frame(first)
query_database()
root.mainloop()
