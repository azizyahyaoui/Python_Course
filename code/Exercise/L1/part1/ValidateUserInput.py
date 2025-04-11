print("---------------------------------------------------------------------------------------")

username = input("Enter your username: ")

if len(username) > 12:
  print("Your username can't be more then 12 characters !")
elif not (username.find(" ") == -1):
  print("Your username can't contain spaces !")
elif not(username.isalpha()):
  print("Your username can contain only alphabets !")
else:
  print(f"Welcome Mr.{username}")

















print("---------------------------------------------------------------------------------------")
