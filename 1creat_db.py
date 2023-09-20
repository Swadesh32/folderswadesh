import mysql.connector
con =mysql.connector.connect(host="localhost",user="subh",passwd="1234@")

mycursor = con.cursor()

mycursor.execute("create database india")






