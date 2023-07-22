# install the mysql https://dev.mysql.com/downloads/installer/
# install myql gui client https://dev.mysql.com/downloads/workbench/
# go to terminal or cmd
# mysql -u root -p 
# show databases

# Related to python
# pip list
# pip install mysql mysql-connector


import mysql.connector

# connect to database of mysql
# mysql port number 3306


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="pydb"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE pydb")
mycursor.execute("CREATE TABLE Persons (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255))");

print(mydb)
#<mysql.connector.connection_cext.CMySQLConnection object at 0x10eba0d00>

# database
# tables
# queries are executed in datbase and tables