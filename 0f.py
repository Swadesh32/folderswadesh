import mysql.connector
con =mysql.connector.connect(host="localhost",user="subh",passwd="1234@")
print(con)
if(con):
    print("connection successful")
else:
    print("connection unsuccessful")    