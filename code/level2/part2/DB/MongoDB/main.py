print("------------------------------------  MongoDB ----------------------------------------------------")

import pymongo



db_connection = pymongo.MongoClient("mongodb://pyadmin:pyadminpassword@localhost:27017/")
db = db_connection["pymongodb-collections"]
collection = db["users"]


try:
    # ✅ CREATE
    def create_user(name, age):
        collection.insert_one({"name": name, "age": age})


    # ✅ READ
    def read_users():
        return list(collection.find({}, {"_id": 0}))


    # ✅ UPDATE
    def update_user(name, new_age):
        collection.update_one({"name": name}, {"$set": {"age": new_age}})


    # ✅ DELETE
    def delete_user(name):
        collection.delete_one({"name": name})


    print("Users:", read_users())  # Read users


    create_user("Alice", 25)
    create_user("Bob", 30)
    create_user("Aziz", 26)

    update_user("Alice", 2886)  # Update Alice's age

    delete_user("Bob")  # Delete Bob

    print("last update Users:", read_users())

except pymongo.errors.ConnectionFailure:
    print("❌ Cannot connect to MongoDB. Check if the server is running!")
except pymongo.errors.OperationFailure as e:
    print(f"❌ Authentication failed! {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

finally:
    db_connection.close()













print()
print("--------------------------------------------------------------------------------------------------------")