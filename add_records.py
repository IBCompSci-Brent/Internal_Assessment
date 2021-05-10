import sqlite3
from tkinter import *

root = Tk()
root.title('Add Record')
root.geometry('500x500')

conn = sqlite3.connect('company.db')
c = conn.cursor()

def enter():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("INSERT INTO records VALUES (:ID, :Name, :Record_Date, :Time_In_Hour, :Time_In_Minute, :Time_Out_Hour, :Time_Out_Minute)",
            {
                'ID': ID.get(),
                'Name': Name.get(),
                'Record_Date': Record_Date.get(),
                'Time_In_Hour': Time_In_Hour.get(),
                'Time_In_Minute': Time_In_Minute.get(),
                'Time_Out_Hour': Time_Out_Hour.get(),
                'Time_Out_Minute': Time_Out_Minute.get()
            })
    conn.commit()
    conn.close()
    ID.delete(0, END)
    Name.delete(0, END)
    Record_Date.delete(0, END)
    Time_In_Hour.delete(0, END)
    Time_In_Minute.delete(0, END)
    Time_Out_Hour.delete(0, END)
    Time_Out_Minute.delete(0, END)

def query():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM records")
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "/n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=4, column=0, columnspan=2)
    conn.commit()
    conn.close()

ID = Entry(root, width=30)
ID.grid(row=0, column=1, padx=20)
Name = Entry(root, width=30)
Name.grid(row=1, column=1)
Record_Date = Entry(root, width=30)
Record_Date.grid(row=2, column=1)
Time_In_Hour = Entry(root, width=30)
Time_In_Hour.grid(row=3, column=1)
Time_In_Minute = Entry(root, width=30)
Time_In_Minute.grid(row=4, column=1)
Time_Out_Hour = Entry(root, width=30)
Time_Out_Hour.grid(row=5, column=1)
Time_Out_Minute = Entry(root, width=30)
Time_In_Minute.grid(row=6, column=1)

ID_label = Label(root, text="ID")
ID_label.grid(row=0, column=0)
Name_label = Label(root, text="Name")
Name_label.grid(row=1, column=0)
Record_Date_label = Label(root, text="Record Date")
Record_Date_label.grid(row=2, column=0)
Time_In_Hour_label = Label(root, text="Time In Hour")
Time_In_Hour_label.grid(row=3, column=0)
Time_In_Minute_label = Label(root, text="Time In Minute")
Time_In_Minute_label.grid(row=4, column=0)
Time_Out_Hour_label = Label(root, text="Time Out Hour")
Time_Out_Hour_label.grid(row=5, column=0)
Time_Out_Minute_label = Label(root, text="Time Out Minute")
Time_Out_Minute_label.grid(row=6, column=0)

enter_btn = Button(root, text="Add Record To Database", command=enter)
enter_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", commmand=query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

conn.commit()
conn.close()

root.mainloop()
