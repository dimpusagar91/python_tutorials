#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect(host="localhost", port=3307, user="root", passwd="giridhar", db="testdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print("Record updated successfully")
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
