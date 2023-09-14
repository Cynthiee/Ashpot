import sqlite3

file = "my_newdb.db"

conn = sqlite3.connect(file)
cursor = conn.cursor()

cursor.execute(
    """ 
    CREATE TABLE IF NOT EXISTS students(
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    age TEXT,
    sex TEXT
    );
    """
)

data = ('Chiemela', 'Uba', 'DD')

cursor.execute(
"""
INSERT INTO students('name', 'age', 'sex')
VALUES(?,?,?)
""", data
)

conn.commit()
cursor.close()
conn.close()