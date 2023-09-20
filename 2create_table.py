import mysql.connector
con =mysql.connector.connect(host="localhost",user="subh",passwd="1234@",database="india")

mycursor = con.cursor()

mycursor.execute(" create table udainfo(emp_id int primary key auto_increment,emp_name varchar(100),designation varchar(100),salary decimal(15,2))")
