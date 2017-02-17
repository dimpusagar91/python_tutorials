import MySQLdb as db
#import mysql.connector as db
#import oursql as db
cnx = db.connect(host="localhost", port=3307, user="root", passwd="giridhar", db="testdb")
cur = cnx.cursor()
cur.execute("SELECT NOW()")
print(cur.fetchall())
cur.close()
cnx.close()
