print("------------------------------------ Files Managing ----------------------------------------------------")

import os # This module provide for python programs to interact with OS

file_path = "code/level2/part1/FilesManaging/test.txt"  # Relative path
file_path2 = "F:/NewProjects/Python/code/level2/part1/FilesManaging/files/test2.txt" #Absolute path
dir_path = "code/level2/part1/FilesManaging/files/"

if os.path.exists(file_path) and os.path.exists(file_path2):
  print(f"The location of '{file_path}' exist.")
  if os.path.isfile:
    print("is a file.")
    print()
  print(f"The location of '{file_path2}' exist.")
else:
  print(f"There is no such file with '{file_path}' !")
  print(f"There is no such file with '{file_path2}' !")

print("__"*50)

if os.path.exists(dir_path):
  print("the directory exist ")
  if os.path.isdir(dir_path):
    print("Is a directory.")
else:
  print(f"There is no such folder with '{dir_path}' !")

print()
print("-------------------------------- Writing Files -----------------------------------")


print()
print("______________________________ Writing txt a File  ____________________________________")

emp_file = "code/level2/part1/FilesManaging/files/output.txt"
Employees = ["Aziz","Bilel","Chiheb","Ghofran"]

try:
  with open(emp_file, "x") as file:  # "w": write(exist or not exist)/ "a" append to exist / "x" write only if not exist
    for emp in Employees:
      file.write(emp + "\n")
    print(f"Txt file '{emp_file}' was created !")
except FileExistsError:
  print(f"this '{emp_file}' file already exist !")


print()
print("______________________________ Writing a json File ____________________________________")

import json

cars_file = "code/level2/part1/FilesManaging/files/cars.json"

cars= {
  1:{"brand": "Ford","model": "Mustang","year": 1964},
  2:{"brand": "Toyota","model": "Corolla","year": 2020},
  3:{"brand": "Honda","model": "Civic","year": 2019}}


try:
  with open(cars_file, "w") as file:
    json.dump(cars, file, indent=4)
    print(f"Json file '{cars_file}' was created !")
except FileExistsError:
  print(f"this '{cars_file}' file already exist !")


print()
print("______________________________ Writing a csv File ____________________________________")

import csv

salta_employees_file = "code/level2/part1/FilesManaging/files/salta_employees.csv"
salta_employees = [["Name", "Age", "Job"],
            ["Spongebob", 30, "Cook"],
            ["Patrick", 37, "Unemployed"],
            ["Sandy", 27, "Scientist"]]

try:
  with open(salta_employees_file, "w") as file:
    writer = csv.writer(file)
    for row in salta_employees:
      writer.writerow(row)
    print(f"Txt file '{salta_employees_file}' was created !")
except FileExistsError:
  print(f"this '{salta_employees_file}' file already exist !")

print()
print("------------------------------- Reading Files -----------------------------------")
print()
print("______________________________ Reading txt a File  ____________________________________")

emp_file = "code/level2/part1/FilesManaging/files/output.txt"

try:
  with open(emp_file, "r") as file:  # r is reading
    file_content = file.read()
    print(file_content)
except FileExistsError:
  print(f"this '{emp_file}' file doesn't exist !")


print()
print("__________________________ Reading txt a File has no permissions ____________________")

no_perm_file ="code/level2/part1/FilesManaging/files/no_perm.txt"

try:
  with open(no_perm_file, "r") as file:  # r is reading
    file_content = file.read()
    print(file_content)
except FileExistsError:
  print(f"this '{no_perm_file}' file doesn't exist !")
except PermissionError:
  print("You do not have permission to read that file")


print()
print("______________________________ Reading a Json File ____________________________________")

cars_file = "code/level2/part1/FilesManaging/files/cars.json"

try:
  with open(cars_file, "r") as car_file:
    cars_file_content = json.load(car_file)
    print(cars_file_content)
except FileExistsError:
  print(f"this '{cars_file}' file doesn't exist !")
except PermissionError:
  print("You do not have permission to read that file")


print()
print("______________________________ Reading a csv File ____________________________________")

salta_employees_file = "code/level2/part1/FilesManaging/files/salta_employees.csv"
try:
  with open(salta_employees_file, "r") as file:
    file_content = csv.reader(file)
    for line in file_content:
      print(line)
      #print(line[0])
except FileExistsError:
  print(f"this '{salta_employees_file}' file doesn't exist !")
except PermissionError:
  print("You do not have permission to read that file")

print()
print("--------------------------------------------------------------------------------------------------------")
