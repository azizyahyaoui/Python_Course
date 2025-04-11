import mysql.connector

print("------------------------------------ MySql DB ----------------------------------------------------")



# Connect to MySQL Server
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pyroot",
    database="pydatabase"
)

cursor = mysql_connection.cursor()

try:

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT
        )
    ''')

    # Insert data
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 30))
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice",30 ))
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alex", 3000))

    mysql_connection.commit()

    # Fetch data
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
         print(row)

    # Update data
    cursor.execute("UPDATE users SET age = %s WHERE name = %s", (35, "Alice"))
    mysql_connection.commit()

    # Fetch data after update
    print("\nUsers After Update:")
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

    # Delete data
    cursor.execute("DELETE FROM users WHERE name = %s", ("Alex",))
    mysql_connection.commit()

    # Fetch data after delete
    print("\nUsers After Delete:")
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)



except mysql.connector.Error as err:
    print(err)
finally:
    # Close the connection
    mysql_connection.close()











print()
print("--------------------------------------------------------------------------------------------------------")