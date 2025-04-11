print("------------------------------------ PostgresQl DB ----------------------------------------------------")

import psycopg2



db_connection = psycopg2.connect(
    dbname="pydatabase",
    user="pyadmin",
    password="pypassword",
    host="localhost",
    port="5432"
)

cursor = db_connection.cursor()
try:
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT
        )
    ''')

    # Insert data
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Charlie", 35))
    db_connection.commit()

    # Fetch data
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    db_connection.close()













print()
print("--------------------------------------------------------------------------------------------------------")