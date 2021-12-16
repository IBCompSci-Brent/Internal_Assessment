import sqlite3
conn = sqlite3.connect('company.db')
conn.execute("PRAGMA foreign_keys = 1")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (
        Username text,
        Passcode text,
        UserID INTEGER PRIMARY KEY
    )""")
c.execute("""CREATE TABLE IF NOT EXISTS departments (
        Name text,
        DepartmentID INTEGER PRIMARY KEY
    )""")
c.execute("""CREATE TABLE IF NOT EXISTS employees (
        Name text,
        DOB text,
        Gender text,
        Department text,
        Position text,
        Phone_Number integer,
        Email text,
        Account text,
        Account_Number integer,
        Social_Security_Number integer,
        Joined text,
        Salary integer,
        EmployeeID INTEGER PRIMARY KEY,
        DepartmentID integer,
        FOREIGN KEY (DepartmentID) REFERENCES departments (DepartmentID)
    )""")
c.execute("""CREATE TABLE IF NOT EXISTS records (
        Name text,
        Record_Date_M integer,
        Record_Date_D integer,
        Record_Date_Y integer,
        Time_In_Hour integer,
        Time_In_Minute integer,
        Time_Out_Hour integer,
        Time_Out_Minute integer,
        RecordID INTEGER PRIMARY KEY,
        EmployeeID integer,
        FOREIGN KEY (EmployeeID) REFERENCES employees (EmployeeID)
    )""")

c.execute("INSERT INTO users VALUES ('Admin','1234',null)")

c.execute("INSERT INTO departments VALUES ('Finance',null)")
c.execute("INSERT INTO departments VALUES ('Human Resources',null)")
c.execute("INSERT INTO departments VALUES ('Sales',null)")
c.execute("INSERT INTO departments VALUES ('Research',null)")

c.execute("INSERT INTO employees VALUES ('James','06-04-04','Male','Finance','CEO','09173236403','james@gmail.com','RCBC','100000000000','1000000000','01-01-21','100',null,1)")
c.execute("INSERT INTO employees VALUES ('John','06-05-04','Male','Human Resources','Manager','09173236404','john@gmail.com','HSBC','200000000000','2000000000','01-02-21','200',null,2)")
c.execute("INSERT INTO employees VALUES ('Chris','06-06-04','Female','Sales','Employee','09173236405','chris@gmail.com','BDO','300000000000','3000000000','01-03-21','300',null,3)")
c.execute("INSERT INTO employees VALUES ('Sam','06-07-04','Male','Research','COO','09173236406','sam@gmail.com','ICBC','400000000000','4000000000','01-04-21','400',null,4)")

c.execute("INSERT INTO records VALUES ('James','03','01','21','9','0','17','0',null,1)")
c.execute("INSERT INTO records VALUES ('John','03','02','21','9','30','17','30',null,2)")
c.execute("INSERT INTO records VALUES ('Chris','03','03','21','10','0','18','0',null,3)")
c.execute("INSERT INTO records VALUES ('Sam','03','04','21','10','30','18','30',null,4)")
c.execute("INSERT INTO records VALUES ('James','04','01','21','9','0','17','0',null,1)")
c.execute("INSERT INTO records VALUES ('John','04','02','21','9','30','17','30',null,2)")
c.execute("INSERT INTO records VALUES ('Chris','04','03','21','10','0','18','0',null,3)")
c.execute("INSERT INTO records VALUES ('Sam','04','04','21','10','30','18','30',null,4)")
c.execute("INSERT INTO records VALUES ('James','03','01','21','9','0','17','0',null,1)")
c.execute("INSERT INTO records VALUES ('John','03','02','21','9','30','17','30',null,2)")
c.execute("INSERT INTO records VALUES ('Chris','03','03','21','10','0','18','0',null,3)")
c.execute("INSERT INTO records VALUES ('Sam','03','04','21','10','30','18','30',null,4)")
c.execute("INSERT INTO records VALUES ('James','04','01','21','9','0','17','0',null,1)")
c.execute("INSERT INTO records VALUES ('John','04','02','21','9','30','17','30',null,2)")
c.execute("INSERT INTO records VALUES ('Chris','04','03','21','10','0','18','0',null,3)")
c.execute("INSERT INTO records VALUES ('Sam','04','04','21','10','30','18','30',null,4)")

conn.commit()
conn.close()
