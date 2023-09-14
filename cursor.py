# import sqlite3

# db_file = "mydb2.db"
# new_connection = sqlite3.connect(db_file)       #  create and connect to db
# my_cursor = new_connection.cursor() # create a cursor

# # Execute an SQL command using the cursor

# my_cursor.execute(
# '''
# CREATE TABLE IF NOT EXISTS students(
# id INTEGER PRIMARY KEY,
# name TEXT,
# age INTEGER,
# sex TEXT
# );
# '''
# )

# students_data =[
#     ('Chiemela', 40, 'male')
#     ('Cynthia', 20, 'female')
# ]

# my_cursor.execute(
# '''
# INSERT INTO students(name, age, sex)
# values(?,?,?)
# ''', 
# students_data)

# new_connection.commit()
# my_cursor.close()

# new_connection.close()



import sqlite3

db_file = "mydt.db"
conn = sqlite3.connect(db_file)       #  create and connect to db
cursor = conn.cursor() # create a cursor

# Execute an SQL command using the cursor

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    age TEXT,
    sex TEXT
    );
    """
)

data = ('Chiemela', 'uu', 'male'),


cursor.execute(
    """
    INSERT INTO students('name', 'age', 'sex')
    VALUES(?,?,?)
    """, data
)
conn.commit()
cursor.close()

conn.close()
