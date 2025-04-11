print("------------------------------------MainPart2---------------------------------------------------")

# List comprehension 
"""  
  A concise way to create lists in Python
  Compact and easier to read than traditional loops
  [expression for value in iterable if condition]

"""

numbers = []

for x in range(1 ,11):
  numbers.append(x * 2)
  
print(numbers)
print()

print("________________ Using  List comprehension ________________")

doubles = [x * 2 for x in range(1, 11)]

print(doubles)
print()
print("___________________")


Even_doubles = [e for e in range(1, 11) if e % 2 == 0]
print(Even_doubles)

Odd_doubles = [o for o in range(1, 11) if not (o % 2 == 0)]
print(Odd_doubles)

print()
print("___________________")
numbers = [1, -2, 3, -4, 5, -6, 8, -7, 9, 10, -11]
positive_nums = [num for num in numbers if num >= 0] # if there is no expression simply just return the value like in this case is "num"  
negative_nums = [num for num in numbers if num < 0]

print(positive_nums)
print(negative_nums)

print()
print("-------------------------------------------------------------------------------------------------")

# Match-case statement (switch): An alternative to using many 'elif' statements
""" 
Execute some code if a value matches a 'case'
Benefits: cleaner and syntax is more readable 

match variable:
    case pattern1:
        # Code for pattern1
    case pattern2:
        # Code for pattern2
    case _:
        # Default case (like 'else')

"""

def check_status(code):
    match code:
        case 200:
            print("Success ✅")
        case 404:
            print("Not Found ❌")
        case 500:
            print("Server Error 🚨")
        case _:
            print("Unknown Status 🤷‍♂️")

check_status(200)
check_status(404)
print("___________________")

def day_of_week(day):
  match day:
    case 1:
      return "It is Sunday"
    case 2:
      return "It is Monday"
    case 3:
      return "It is Tuesday"
    case 4:
      return "It is Wednesday"
    case 5:
      return "It is Thursday"
    case 6:
      return "It is Friday"
    case 7:
      return "It is Saturday"
    case _:
      return "Not a valid day"

print(day_of_week("pizza"))

print("___________________ With or '|' ___________________ ")
def check_day(day):
    match day:
        case "Saturday" | "Sunday":
            print("It's the weekend! 🎉")
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print(" blues! 😴")
        case _:
            print("It's a weekday! 🏢")

check_day("Sunday")

print()
print("-------------------------------------------------------------------------------------------------")

# Modules ==> # module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files

# print(help("modules"))

""" 
import math 
or
import math as m // making m an alias for math nice thing for long modules names
or
from math import pi // is not the recommended cause may lied to conflict with other vars or methods in the prog
"""
import math as m
print(m.pi)

print("___________________ 'User-defined Module' ___________________ ")

import modules.example_module as my_md

result = my_md.power(5)
print(result)

result = my_md.cube(5)
print(result)

result = my_md.circumference(5)
print(result)

result = my_md.area(5)
print(result)

print()
print("-------------------------------------------------------------------------------------------------")

# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

from math import e # built-in variable

print(e)  # built-in variable

def func1():
    e = 8 # local variable                 
    print(e)
    def inner_func1():
        e = 5 # enclosed variable              
        print(e)
    inner_func1()

e = 3 # global variable                       

func1()

print()
print("-------------------------------------------------------------------------------------------------")


# if __name__ == "__main__":  # if the script is run directly
# Functions and classes in this module can be reused without the main block of code executing
""" 
Good practice (code is modular,
              helps readability,
              leaves no global variables,
              avoid unintended execution)

library = import library for functionality
Ex.

main : (this script can be imported OR run standalone)

When running library directly, display a help page 

"""
import Scripts.script1 as s1
import Scripts.script2 as s2
def main():
    s1.print_hello1()
    s2.print_hello2()
    print("Hello from main()")
    print("This is the main module")

if __name__ == "__main__":
    main()

print()
print("___________________\" \" _________________________")

print()
print("-------------------------------------------------------------------------------------------------")