# write a function that will create a database
# and insert data into it

# import sqlite3

# def new_db():
#     file = 'filedt.db'

#     conn = sqlite3.connect(file)
#     cursor = conn.cursor()

#     cursor.execute(
#     """ 
#     CREATE TABLE IF NOT EXISTS staff(
#     employee_id INTEGER PRIMARY KEY,
#     name TEXT,
#     age TEXT,
#     sex TEXT
#     );
#     """
# )
#     data =[
#     ('Chibuike', '30', 'M'),
#     ('Cynthia', '23', 'F'),
#     ('Jennifer', '20', 'F'),
#     ('Paul', '12', 'M')
#     ]
#     cursor.executemany(
#     """
#     INSERT INTO staff('name', 'age', 'sex')
#     VALUES(?,?,?)

#     """, data
#     )

#     conn.commit()
#     cursor.close()
#     conn.close()
# new_db()



import sqlite3

def create_table():
    file = 'filedt.db'

    conn = sqlite3.connect(file)
    cursor = conn.cursor()

    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS staff(
            employee_id INTEGER PRIMARY KEY,
            name TEXT,
            age TEXT,
            sex TEXT
        );
        """
    )

   

def insert_data(data):
    file = 'filedt.db'

    conn = sqlite3.connect(file)
    cursor = conn.cursor()

    cursor.executemany(
        """
        INSERT INTO staff(name, age, sex)
        VALUES(?, ?, ?)
        """, data
    )

    conn.commit()
    cursor.close()
    conn.close()

def select_data():
    file = 'filedt.db'

    conn = sqlite3.connect(file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM staff")
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_data(employee_id, new_age):
    file = 'filedt.db'

    conn = sqlite3.connect(file)
    cursor = conn.cursor()

    cursor.execute("UPDATE staff SET age = ? WHERE employee_id = ?", (new_age, employee_id))

    conn.commit()
    conn.close()

def delete_data(employee_id):
    file = 'filedt.db'

    conn = sqlite3.connect(file)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM staff WHERE employee_id = ?", (employee_id,))

    conn.commit()
    conn.close()

# Create the table
create_table()

# Insert data
data = [
    ('Chibuike', '30', 'M'),
    ('Cynthia', '23', 'F'),
    ('Jennifer', '20', 'F'),
    ('Paul', '12', 'M')
]
insert_data(data)

# Select data
result = select_data()
print("Data in the database:")
for row in result:
    print(row)

# Update data
update_data(1, '31')

# Delete data
delete_data(4)

