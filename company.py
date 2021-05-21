import sqlite3
conn = sqlite3.connect('company.db')
conn.execute("PRAGMA foreign_keys = 1")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS departments (
        Name text
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
        Joined integer
    )""")
c.execute("""CREATE TABLE IF NOT EXISTS records (
        Name text,
        Record_Date_M integer,
        Record_Date_D integer,
        Record_Date_Y integer,
        Time_In_Hour integer,
        Time_In_Minute integer,
        Time_Out_Hour integer,
        Time_Out_Minute integer
    )""")

c.execute("INSERT INTO departments VALUES ('Finance')")
c.execute("INSERT INTO departments VALUES ('Human Resources')")
c.execute("INSERT INTO departments VALUES ('Sales')")
c.execute("INSERT INTO departments VALUES ('Research')")

c.execute("INSERT INTO employees VALUES ('Brent','06-04-04','Male','Finance','CEO','09173236403','brent.tai@britishschoolmanila.org','RCBC','100000000000','1000000000','010121')")
c.execute("INSERT INTO employees VALUES ('Hari','06-05-04','Male','Human Resources','Manager','09173236404','hari.denton@britishschoolmanila.org','HSBC','200000000000','2000000000','010221')")
c.execute("INSERT INTO employees VALUES ('Kristen','06-06-04','Female','Sales','Employee','09173236405','kristen.tan@britishschoolmanila.org','BDO','300000000000','3000000000','010321')")
c.execute("INSERT INTO employees VALUES ('Vince','06-07-04','Male','Research','COO','09173236405','vince.tiu@britishschoolmanila.org','ICBC','400000000000','4000000000','010421')")

c.execute("INSERT INTO records VALUES ('Brent','03','01','21','9','0','17','0')")
c.execute("INSERT INTO records VALUES ('Hari','03','02','21','9','30','17','30')")
c.execute("INSERT INTO records VALUES ('Kristen','03','03','21','10','0','18','0')")
c.execute("INSERT INTO records VALUES ('Vince','03','04','21','10','30','18','30')")

conn.commit()

