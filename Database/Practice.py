# mandatory code: Building a connection and a cursor for MySQL

import mysql.connector
conn= mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='5_Arbhqw',
    database= 'amazon'# to select amazon database
)
cur = conn.cursor()
#print(cur)

#==========================================================

#How to create Database.
'''
sql= "create database Flipkart;"
cur.execute(sql)

# To select amazon database however we define it above already so no need to repeatthe connection again and again
sql="use amazon"
cur.execute(sql)

#How to create a Table


query= "create table employee(eid INT,ename VARCHAR(100), eadd VARCHAR(100),esal Decimal(8,2));"
cur.execute(query)

# To update data in Employee table

sql= "insert into employee value(101,'Rahul Kumar','Noida',765434.34)"
cur.execute(sql)
conn.commit() #  If there is any change in database we need to tell connection to commit

#upload data 

eid=input("Enter the Employee ID: ")
ename=input("Enter the name of Employee: ")
eadd=input("Enter the address of employee: ")
esal=input("Enter the salary: ")

sql="insert into employee value(%s,%s,%s,%s)"
data = (eid,ename,eadd,esal)
cur.execute(sql,data)
conn.commit()

# How to read data


sql ="select * from employee"
cur.execute(sql)
data= cur.fetchall()
for emp in data:
    print(emp[0], '\t', emp[1],'\t',emp[2],'\t',emp[3])

    
# Delete data from Table
sql= 'delete from employee where eid=102'
cur.execute(sql)
conn.commit()
'''
#Update data in table

sql= "update employee set esal=70000 where eid=103"
cur.execute(sql)
conn.commit()


