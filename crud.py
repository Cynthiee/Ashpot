import sqlite3

try:
    def create_table():
        crud_file = 'crud.db'

        connection = sqlite3.connect(crud_file)
        cursor = connection.cursor()

        cursor.execute(
            """ CREATE TABLE IF NOT EXISTS actors(
            employee_id INTEGER PRIMARY KEY,
            name    TEXT,
            age TEXT,
            gender TEXT
            );
            """
        )
    def insert_data(data):
        crud_file = 'crud.db'    

        connection = sqlite3.connect(crud_file)
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO actors( name, age, gender)
            VALUES(?, ?, ?)
            """, data
        )
        connection.commit()
        cursor.close()
        connection.close()
        
    def select_data():
        crud_file = 'crud.db'    

        connection = sqlite3.connect(crud_file)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM staff")
        record = cursor.fetchall()
        print("Cruddb contents", record)

        connection.close()

    def update_data(employee_id, new_age):
        crud_file = 'crud.db'    

        connection = sqlite3.connect(crud_file)
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE actors SET age = ? WHERE employee_id = ?",
            (new_age, employee_id))
        
        connection.commit()
        connection.close()

    def delete_data(employee_id):
        crud_file = 'crud.db'    

        connection = sqlite3.connect(crud_file)
        cursor = connection.cursor()

        cursor.execute("DELETE FROM actors WHERE employee_id = ?", (employee_id))

        connection.commit()
        connection.close()

    create_table()

    data = [
        ('Genevieve', '30', 'M'),
        ('Ruth', '23', 'F'),
        ('Uche', '20', 'F'),
        ('Adewale', '12', 'M')
    ]
    insert_data(data)

    result = select_data()
    print("Data in the database:")
    for record in result:
        print(record)

    update_data(1, '31')
    delete_data(4)
except:
    