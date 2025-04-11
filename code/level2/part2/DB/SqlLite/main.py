print("------------------------------------ SqlLite DB ----------------------------------------------------")

import sqlite3

data_path = "code/level2/part2/DB/SqlLite/data/users.db"
# Connect to (or create) a database file
db_connection = sqlite3.connect(data_path)
cursor = db_connection.cursor()

try:

  # CREATE TABLE
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          age INTEGER
      )
  ''')

  db_connection.commit()
  # ✅ CREATE (INSERT)
  def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    db_connection.commit()
    print("--------------------------")
    print("Data created successfully!")
    print("--------------------------")


  # ✅ READ (SELECT)
  def read_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()



  # ✅ UPDATE
  def update_user(id, new_age):
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, id))
    db_connection.commit()
    print("--------------------------")
    print("Data updated successfully!")
    print("--------------------------")


  # ✅ DELETE
  def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    db_connection.commit()
    print("--------------------------")
    print("Data deleted successfully!")
    print("--------------------------")


  # Example Usage
  create_user("Alice", 120)
  create_user("Bob", 30)
  create_user("Charlie", 35)
  create_user("David", 35)


  print("--------------------------")
  print("Users:", read_users())  # Read and display users
  print("--------------------------")

  update_user(1, 26)  # Update Alice's age
  delete_user(2)  # Delete Bob

  print("--------------------------")
  print("Updated Users:", read_users())
  print("--------------------------")


except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
  db_connection.close() # Close connection












print()
print("--------------------------------------------------------------------------------------------------------")