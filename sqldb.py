import os
import sqlite3


my_file = "mydb.db"
if os.path.exists(my_file):
    print('File exists')
else:
   print('Find file')
try:
    conn = sqlite3.connect(my_file)
    print("Database created")
    print('Database already exist.')
except:
    print('Unable to connect to database')
finally:
    if conn:
        conn.close()

conn.cursor()
cursor.execute()