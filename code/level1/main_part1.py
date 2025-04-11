#Python rechecking

print("Hello Python we back again ")



print("---------------------------------------------------------------------------------------")

# variables in python [integers, floats, strings, and booleans]

first_name = "Yahyaoui"
last_name = "aziz"
age = 28
email = "aziz@gmail.com"
hight = 1.75
is_dev = True

print(f"Hello {first_name} {last_name}")
print(f"Your age is: {age} years old")
print(f"Your current email is: {email} ")
print(f"your hight is: {hight} cm")
print(f"Is you're a developer: {is_dev}")


print("---------------------------------------------------------------------------------------")

# Type casting [str(), int(), float(), bool()]

name = " anything"
num = 125
price = 13.5
is_student = True

print("type of name", type(name))
print("type of num", type(num))
print("type of price", type(price))
print("type of is_student", type(is_student))

print("_______________________________")


num = float(num)
price = int(price)

print("num value",num)
print("type of num", type(num))
print("price value",price)
print("type of price", type(price))

num = str(num)
print("num value",num)
print("type of num", type(num))

print("---------------------------------------------------------------------------------------")

# Data user input

#customer_name = input("Enter your name plz: ")
#customer_age = int(input("What is your age? ")) # if u gonna use the input in numeric operation u should type cast it

#print(f"Hello Mr/Ms. {customer_name}")
#print(f"your current age is: {customer_age}")

#customer_age += 1
#print(f"Next year your age will be: {customer_age}")

print("---------------------------------------------------------------------------------------")

#  Math in Python
# +=,-=,*=;/=,%=,**=

number =5
number +=2
print(f" number + 2 = {number}")
number %= 2
# %: remainder
print(f" number % 3 = {number}")
number = 7
number /= 3
print(f" number / 3 = {number}")
number = 7
number **= 2
print(f" number² = {number}")

print("_______________________________")

# Math Functions

x = 3.14
y = -5
z = 7

result = round(x)
print(f"round X({x}) = {result}")
result = abs(y)
print(f"absolute Y({y}) = {result}")
result = pow(z, 2)
print(f" Z({z}) power 2  = {result}")
result = max(x, y, z)
print(f"max between X({x}), Y({y}) and Z({z}) is {result}")
result = min(x, y, z)
print(f"min between X({x}), Y({y}) and Z({z}) is {result}")

print("_______________________________")

# These function need to import the math lib to utilize them
import math

print(f"The value of Pi(π) = {math.pi}")
print(f"the value of The base of the natural logarithm and exponential = {math.e}")

a = 9
print(f"the root of a({a}) = {math.sqrt(a)}")
b = 9.9
print(f"the ceil of b({b}) = {math.ceil(b)}")
c = 9.9
print(f"the floor of c({c}) = {math.floor(c)}")

print("---------------------------------------------------------------------------------------")

# if, if-else, if-elif-else, Nested if, if Ternary Operator

#respond = input("Are u hungry ? (Y/N): ")
respond = "N"

if respond == "y" or respond == "Y" or respond == "yes" or respond == "Yes":
  print("Have some food.")
else:
  print("No food for you now !")

print("_______________________________")

is_online = False

if is_online :                    # "if is_online :" or "if is_online == "True" :"
  print("The user is online.")
else:
  print("The user is offline!")


print("_______________________________")

marks = 101

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

print("_______________________________")

num = 11

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number or zero")

print("______________________________________________")

# return X if (condition) else return Y

age = 20
status = "Adult" if age >= 18 else "Minor"
print("Your status is",status)

print("_________________________________")

my_num = 5
result = "EVEN" if my_num % 2 == 0 else "ODD"
print(f"The given number is:{result} ")

print("_________________________________")

#user_role = "admin"
user_role = "guest"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(f"the user with the role '{user_role}', has a: {access_level}")

print("---------------------------------------------------------------------------------------")


# Logical operator or , and, not

age = 28 #int(input("Enter your age: ")) 
is_student = True #input("Are you a student? (yes/no): ")
has_coupon = True #input("Do you have a discount coupon? (yes/no): ")

if (age < 18 or is_student) and not has_coupon:
    print("You are eligible for a student discount!")
elif has_coupon:
    print("You are eligible for a discount with your coupon!")
else:
    print("Sorry, you are not eligible for a discount.")

print("---------------------------------------------------------------------------------------")
# String Methods

# list all the methods
#print(help(str))

# String length: `len()`

msg = "hello world"
length = len(msg)
print("the sting length is: ",length)

print("______________________________________________")
# Changing case (`upper()`, `lower()`, `title()`,`capitalize()`)

print(msg.upper()) 
print(msg.lower()) 
print(msg.capitalize())
print(msg.title())

print("______________________________________________")
#Finding and replacing substrings (`find()`,`count()`, `replace()`)

find_space = msg.find(" ")
print(f"The space character found in: {find_space}")
find_last_o = msg.rfind("o")
print(f"The last 'o' character found in: {find_last_o}")

l_count = msg.count("l")
print(f"There're {l_count} 'L' in '{msg}'")

new_msg = msg.replace("world", "there!. 'Kenobi'")
print(new_msg)

print("______________________________________________")
#Checking string content (`isdigit()`, `isalpha()`, `isalnum()`)

f_num = "15551"
is_msg_dig = msg.isdigit()
print(f"is the msg digit: {is_msg_dig}")
is_f_num_dig = f_num.isdigit()
print(f"is the f_num digit: {is_f_num_dig}")
is_msg_alpha = msg.isalpha()
print(f"is the msg alpha: {is_msg_alpha}")
text = "CVE12588"
is_text_alnum = text.isalnum()
print(f"is text contains alpha and digits: {is_text_alnum}")

print("______________________________________________")
# Formatting strings (`format()`, `f-strings`)

name = "Alice"
age = 25
print("My name is",name,"and I am",age,"years old." )
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")


print("______________________________________________")
# Splitting and joining (`split()`, `join()`, `strip()`)

text = "apple,banana,orange"
print(text.split(","))  # Output: ['apple', 'banana', 'orange']

words = ["Hello", "World", "Python"]
print(" ".join(words))  # Output: "Hello World Python"

text = "   Hello World   "
print(text.strip())  # Output: "Hello World"
print("---------------------------------------------------------------------------------------")

# String indexing [Start: End: Step]

credit_card = "1234-5678-9024-5623"

print(credit_card[:4])  # [0:4]
last_digits = credit_card[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
reverse_credit_card = credit_card[::-1]
print(f"reversed: {reverse_credit_card} ") 

print("---------------------------------------------------------------------------------------")

# Format specifiers

number1 = 8948.1266
number2 = -895
number3 = 121112

print(f"number1: {number1:+,.2f}")
print(f"number2 {number2:>10}")
print(f"number2 {number2:^10}")
print(f"number2 {number2:.2f}")
print(f"number3 {number:o}")
print(f"number3: {number3:b}")

print("---------------------------------------------------------------------------------------")

# Loops:

# while true do

place_holder = "Java" #input("Enter your favorite language: ")
while place_holder == "" :
    print("Sure u do love language ple enter one at least")
    place_holder = input("Enter your favorite language: ")

print(f"Your fav prog language is: {place_holder}")

print("______________________________")



""" food = input("Enter your fav food (q to quit): ")

while not food == "q":
    if not food == "":
        print(f"you like {food}")
        food = input("What else you do like (q to quit): ")
    else:
        food = input("What else you do like (q to quit): ")

print("Have a nice meal!") """

print("______________________________")

""" p_number = int(input("Enter a number between 1 - 10: "))
while p_number <1 or p_number > 10:
    print(f"{p_number} is not valid !")
    p_number = int(input("Enter a number between 1 - 10: "))

print(f"Your number is: {p_number}") """

print("______________________________________________")

# For loop used with fixed number of times

for i in range(1, 10):
    print(f"i[{i}]") 
print("______________________________")
# reversed
for j in reversed(range(1, 10)):
    print(f"j[{j}]") 
print("______________________________")
#With step

for i in range(1, 10, 3):
    print(f"i[{i}]")

print("______________________________")

msg = "Happy New Year !"
c = 0
for m in msg:
    print(f"char[{c}]= {m}")
    c +=1

print("______________________________")

msg = "Happy New Year !"
c = 0
for m in msg:
    if m == " ":
        break # or continue
    else:
        print(f"char[{c}]= {m}")
        c +=1

print("______________________________")

# Nested loop (outer, inner)

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    
    print()


print("______________________________")

rows= 3
columns = 5
symbol = "-"
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    
    print()

print("---------------------------------------------------------------------------------------")

# Collections (List, Set, Tuple, Dict)

""" 
    collection = single "variable" used to store multiple values
    List = [] ordered and changeable. Duplicates OK
    Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
    Tuple = () ordered and unchangeable. Duplicates OK. FASTER
    Dict =  {"key":"value"} , pairs ordered and changeable. No duplications
"""

print("____________________List________________________")

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[0])
print(fruits[::-1])
print(fruits[::2])
print(fruits[:3:])

print("______________________________")

for fruit in fruits:
    print(fruit)

print("______________________________")
# print(help(fruit))  # print all the method that used with the set collection as sort(), len(), in():bool

fruits.sort()
print("sorted:")
for fruit in fruits:
    print(fruit)

print("______________________________")
size = len(fruits)
print(f"Size of the list: {size} elements.")
print("______________________________")
is_contains = "apple" in fruits
print(f"is fruits contains apple: {is_contains}")

print("______________________________")
fruits[0] = "pineapple"
for fruit in fruits:
    print(fruit)

fruits[0] = "pineapple"

print("______________________________")

fruits = ["apple", "orange", "banana", "coconut"]

fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "fig")
print(fruits)
fruits.reverse()
print(fruits)
print(f"index of coconut: {fruits.index("coconut")} ")
print(fruits.count("apple"))
fruits.clear()
print(fruits)

print()
print("____________________2D List_____________________")

""" 
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats] 
"""

groceries = [["apple", "orange", "banana", "coconut"],
            ["celery", "carrots", "potatoes"],
            ["chicken", "fish", "turkey"]]

print(groceries)
print(groceries[2][1])
print(groceries[1])
#using nested loop

print("using nested loop:")
for coll in groceries:
    for food in coll:
        print(f"{food}",end="   ")
    print()
print()

print("____________________Set_________________________")

fruits = {"apple", "orange", "banana", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
fruits.pop()

print(fruits)
#for fruit in fruits:

print()
print("____________________Tuple_______________________")

fruits = ("apple", "orange", "banana", "coconut", "coconut")
# print(dir(fruits))
# print(help(fruits))
print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple")  ===> cant change a tuple
# fruits.remove("apple")
# fruits.pop()
print(fruits)

print()
print("____________________Dict________________________")

# dict {key, val}

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "Tunisia": "Tunisia",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))

# get val using key
print(f"The capital of the USA: {capitals.get("USA")}")

#if there is no such value or key ==> None
print(f"The capital of the Japan: {capitals.get("Japan")}")

#using if
if capitals.get("Japan"):
    print("The capital exist in the dict.")
else:
    print("Doesn't exist!")

if capitals.get("Russia"):
    print("The capital exist in the dict.")
else:
    print("Doesn't exist!")

# Methods
capitals.update({"Germany": "Berlin"}) # Adding new line
capitals.update({"Tunisia": "Kairouan"}) # update an exist one
print(capitals)
print()

""" capitals.pop("China") # delete an item
print(capitals)
print()

capitals.popitem() # delete last item
print(capitals)
print()

capitals.clear() # empty
print(capitals)
print() """

# return all keys
keys = capitals.keys() 
print(keys) # return object contains list
for k in keys:
    print(k, end=" ")
print()

print()
# return all values
values = capitals.values() 
print(values) # return object contains list
for v in values:
    print(v, end=" ")
print()

print()


# return all items
items = capitals.items()
print(items) # return object contains list
print()
for k , v in items:
    print(f"{k}: {v}")
print()
print("---------------------------------------------------------------------------------------")

# Random
import random

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")

ran_number = random.randint(low, high)
print(ran_number)
ran_number = random. random()
print(ran_number)
option = random.choice(options)
print(option)

print("____________________Shuffle:________________________")

deck_cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]

random.shuffle(deck_cards)
print(deck_cards)

print()
print("---------------------------------------------------------------------------------------")

# Functions()

"""
def function_name():
    # Function body
    # Code to execute 
"""

def say_hello():
    print("Hello from func in python.")
    print("end func!")

say_hello()

print("____________________________________________")

# Function with parameters or arguments
"""
def function_name(parameters):
    # Function body
    # Code to execute 
"""

def greeting(name):
    print(f"Hello Mr.{name}")

greeting("Aziz")

print("____________________________________________")

def display_invoice(username:str, amount:float, due_date:str):
    print(f"Hello Mr.{username}.")
    print(f"Your bill of ${amount:.2f} is due: {due_date}.")

display_invoice("Yahyaoui Aziz", 100.25, "05/21")

print("____________________________________________")

# Function with return statement

"""
def function_name(parameters):
    # Function body
    # Code to execute 
    # return value
"""
def full_name(first_name:str , last_name:str):
    first_name = first_name.capitalize()
    last_name =last_name.capitalize()
    f_name = first_name + " " + last_name
    return f_name 

print(full_name("Yahyaoui", "Med Aziz"))

print("____________________________________________")

"""
default arguments = A default value for certain parameters
    default is used when that argument is omitted
    make your functions more flexible, reduces # of arguments
    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

"""
def net_price(list_price, discount=0, tax=0.05):
    return list_price *(1 - discount) * (1 + tax)

print(f"Client 1 has no discount with default tax, final price is: ${net_price(500)} .") 
print(f"Client 2 has a capon of 10% discount with default tax, final price is: ${net_price(800,0.1)} .")
print(f"Client 3 has a gol capon 10% discount with 0 tax, final price is: ${net_price(550,0.1,0)} .")

print("____________________________________________")

import time

def count(end, start=0): # count(start=0, end) wrong ==> cause an arg with a default value shouldn't place as the first arg
    for x in range(start, end+1):
        print(x,end=" ")
        time.sleep(1)
    print("DONE!")

count(2)

print("____________________________________________")
# keyword arguments = an argument preceded by an identifier
""" helps with readability
order of arguments doesn't matter
1. positional 2. default 3. KEYWORD 4. arbitrary
"""

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)

print("___________________\"*args\" _________________________")

# "*args" = allows you to pass multiple non-key arguments. And "*args" is of type tuple.
# "**kwargs" = allows you to pass multiple keyword-arguments. And "**kwargs" is of type dictionary.
"""
    unpacking operator
    1. positional 2. default 3. keyword 4. ARBITRARY 
"""

def add(*nums):
    total = 0
    for arg in nums:
        total += arg
    return total

print(add(1))
print(add(1 + 5))
print(add(1 + 5 + 4 + 6))

print("___________________\"**kwargs\" _________________________")

def home_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key:3}: {value}.")

home_address(street = "125 Fake st.",
            building = "C3",
            apartment = 40,
            city = "Bargou",
            state ="Siliana",
            zip = "61111444"
            )

print("___________________Using both \"*args\" & \"**kwargs\" _________________________")

def shipping_order(*args, **address):
    for arg in args:
        print(arg, end =" ")
    print()

    for key,value in address.items():
        print(f"{key:3}: {value}.")
    print()

shipping_order("Mr.", "Yahyaoui", "Med Aziz",
            street = "125 Fake st.",
            building = "C3",
            apartment = 40,
            city = "Bargou",
            state ="Siliana",
            zip = "61111444"
            )

print()
print("---------------------------------------------------------------------------------------")

"""
    Iterables = An object/collection that can return its elements one at a time,
    allowing it to be iterated over in a loop
    As str, lists, tuples, sets and dict.
"""

list_number = [1,2,3,4,5,6]

for it_num in list_number:
    print(it_num, end= "-")

print()

str = "Hello there!"

for it_str in str:
    print(it_str, end= "-")

print()

my_dict = {"A": 1, "B": 2, "C": 3,"D": 4}

for key, value in my_dict.items():
    print(f"{key}: {value}")

print()
print("---------------------------------------------------------------------------------------")


# Membership operators = used to test whether a value or variable is found in a sequence
""" 
    (string, list, tuple, set, or dictionary)
    1. in
    2. not in
"""

word = "apple"
def guess_letter(letter):
    if letter in word:
        print(f"There is a {letter}")
    else:
        print(f"{letter} was not found")


guess_letter("a")
guess_letter("z")
guess_letter("l")

print()
print("___________________\"IS NOT IN:\" _________________________")

word = "coffee"
def guess_letter_not_in(letter):
    if letter not in word:
        print(f"{letter} was not found")
    else:
        print(f"There is a {letter}")


guess_letter("c")
guess_letter("b")
guess_letter("g")

print()
print("___________________________________________________")

grades = {
        "Sandy": "A",
        "Squidward": 
        "B","Spongebob":
        "C","Patrick": "D"
        }

student = "Spongebob" #input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

print()
print("---------------------------------------------------------------------------------------")