print("------------------------------------OOP ---------------------------------------------------")

# object = A "bundle" of related attributes (variables)I and methods (functions)
# Ex. phone, cup, book
# You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object


class Car: # same as java class the class name should start with capital letter
    
    # constructor
    def __init__(self, color, brand, model, year):
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year


    # methods
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def drive(self):
        print("Car is driving")

    def park(self):
        print("Car is parked")
    
    def display_info(self):
        print(f"Color: {self.color}, Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

car = Car("Red", "Toyota", "Corolla", 2020) # instantiating the class
car.start() # calling the method
car.drive()
car.stop()
car.display_info()
car2 = Car("Blue", "Honda", "Civic", 2019)
car2.display_info()

print()
print("______________________________Import from separate class ____________________________________")
from classes.person import Person
person = Person("John", 30, "Engineer")
person.display_info()
person2 = Person("Jane", 25, "Doctor")
person2.display_info()

print()
print("______________________________Class variables ____________________________________")
# Class variables are shared among all instances of a class
# Instance variables are unique to each instance of a class
# Define class variables outside of any method in the class even outside of the constructor
# Access class variables using the class name
# Allows you to define attributes that are shared among all instances of a class
# Ex. number of objects created from a class

import classes.student as student
student1 = student.Student("John", 30, "Engineer")
student1.display_info()
student2 = student.Student("Jane", 25, "Doctor")
student2.display_info()
student3 = student.Student("Alice", 22, "Nurse")
student3.display_info()
student4 = student.Student("Bob", 28, "Teacher")
student4.display_info()
print(f"Number of students: {student.Student.number_of_students} in class year {student.Student.class_year}")

print()
print("______________________________ Inheritance ____________________________________")
# Inheritance allows you to define a class that inherits all the methods and properties from another class
# The class that inherits is called the child class and the class that is inherited from is called the parent class
# Child class can override the methods and properties of the parent class and can also add new methods and properties

""" 
  - Ex. Car class and ElectricCar class
  - ElectricCar class inherits from Car class
  - ElectricCar class has all the methods and properties of Car class
  - ElectricCar class can have additional methods and properties
  - ElectricCar class can override methods and properties of Car class
  - ElectricCar class can have its own constructor
  - ElectricCar class can have its own class variables 
"""
import classes.cat as cat
import classes.dog as dog

cat_siam = cat.Cat("Siam", "Siamese")
cat_siam.show_name()
cat_siam.walk()
cat_siam.eat()
cat_siam.sleep()
cat_siam.sound()
dog_buddy = dog.Dog("Buddy", "Golden Retriever")
dog_buddy.show_name()
dog_buddy.walk()
dog_buddy.eat()
dog_buddy.sleep()
dog_buddy.sound()

print()
print("______________________________ Multiple/Multilevel Inheritance ____________________________________")
# multiple inheritance = inherit from more than one parent class
#                     C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                     C(B) <- B(A) <- A

from classes.predator import Predator
from classes.prey import Prey

class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass

class fish(Prey, Predator):
    pass

hawk = Hawk("Hawk", "Bird")
hawk.show_name()
hawk.walk()
hawk.eat()
hawk.sleep()
hawk.hunt()
rabbit = Rabbit("Rabbit", "Mammal")
rabbit.show_name()
rabbit.walk()
rabbit.eat()
rabbit.sleep()
rabbit.flee()
fish1 = fish("Fish", "Aquatic")
fish1.show_name()
fish1.walk()
fish1.eat()
fish1.sleep()
fish1.hunt()
fish1.flee()

print()
print("______________________________ Super() Inheritance ____________________________________")
# super() function = used to call the parent(superclass) class's constructor
# super() function = also used to call the parent class's methods
# super() function = returns a temporary object of the superclass that allows you to call the superclass's methods
# super() function = used to call the superclass's constructor and initialize the superclass's attributes

class Shape:

    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"Color: {self.color}, Is filled: {self.is_filled}")


class Circle(Shape):

    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"Radius: {self.radius}")

class Triangle(Shape):

    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"width: {self.width}, Height: {self.height}") # overriding the describe method

class Square(Shape):

    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side
    


Circle1 = Circle("Red", True, 5)
Circle1.describe()
Triangle1 = Triangle("Blue", False, 10, 5)
Triangle1.describe()
Square1 = Square("Green", True, 10)
Square1.describe()

print()
print("______________________________ Polymorphism ____________________________________")
# Polymorphism = means many shapes
# Polymorphism = allows you to define methods in the child class with the same name as defined in their parent class
# Polymorphism = allows you to perform a single action in different ways
# Tow ways to achieve polymorphism: inheritance and duck typing

from classes.c_circle import C_Circle
from classes.c_triangle import C_Triangle

shapes = [C_Circle(5), C_Triangle(10, 5)]
for shape in shapes:
    shape.print_area()


print()
print("__________________ Duck Typing __________________")
"""  
"Duck typing" = Another way to achieve polymorphism besides Inheritance
    Object must have the minimum necessary attributes/methods
    "If it looks like a duck and quacks like a duck, it must be a duck."
"""
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

    alive = False

    def speak(self):
        print("VROOM!")

creatures = [Dog(), Cat(), Car()]
for creature in creatures:
    creature.speak()
    print(f"Alive: {creature.alive}")

print()
print("______________________________ Static Methods ____________________________________")

""" 
@staticmethod 
        - Static methods = A method that belong to a class rather than any object from that class (instance)
                Usually used for general utility functions

        - Instance methods = Best for operations on instances of the class (objects)
        - Static methods = Best for utility functions that do not need access to class data
"""

class Employee:
    def __init__(self, first_name, last_name, salary, position):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.position = position
    
    @staticmethod
    def is_valid_position(position):
        positions = ["Manager", "Developer", "Designer", "Engineer"]
        return position in positions

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}, Salary: {self.salary}, Position: {self.position}")

employee1 = Employee("John", "Doe", 50000, "Developer")
employee1.display_info()
print(Employee.is_valid_position("Developer"))
employee2 = Employee("Jane", "Smith", 60000, "chemist")
employee2.display_info()
print(Employee.is_valid_position("chemist"))
employee3 = Employee("Eugene", "Potter", 70000,"engineer")
employee3.display_info()
print(Employee.is_valid_position("engineer"))

print()
print("______________________________ Class Methods ____________________________________")
"""
@classmethod

Class methods = Allow operations related to the class itself
Take (cls) as the first parameter, which represents the class itself.
"""

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"
    
    @classmethod
    def get_number_of_student(cls):
        return f"Number of students: {cls.count:2f}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count}"

student1 = Student("John", 3.5)
print(student1.get_info())
print(Student.get_number_of_student())
student2 = Student("Jane", 3.7)
print(student2.get_info())
student3 = Student("Alice", 3.9)
print(student3.get_info())
print(Student.get_number_of_student())
print(Student.get_avg_gpa())

print()
print("______________________________ Magic Methods ____________________________________")
""""
Magic methods = Special methods that start and end with double underscores
                Also called dunder methods
                Used to emulate built-in behavior within Python
                Ex. __init__, __str__, __add__, __len__, __eq__, __lt__, __gt__, __del__, __iter__, __next__, __getitem__, __setitem__, __delitem__
They are automatically called by many of Python's built-in operations.
They allow developers to define or customize the behavior of objects

"""
class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author and self.pages == value.pages
    
    def __lt__(self, value):
        return self.pages < value.pages
    
    def __gt__(self, value):
        return self.pages > value.pages
    
    def __add__(self, value):
        return self.pages + value.pages
    
    def __contains__(self, value):
        return value in self.title or value in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return None

    """ def __del__(self):
        print("Book deleted") """

book1 = Book("Python Programming", "John Doe", 300)
book2 = Book("Java Programming", "Jane Smith", 400)
book3 = Book("The Art of War", "Sun Tzu", 200)
book4 = Book(" the hobbit", "J.R.R. Tolkien", 500)

print(book1)
print(len(book1))
print(book1 == book2)
print(book1 == book1)
print(book1 < book2)
print(book1 > book2)

print(book3["title"])

print()
print("______________________________ Property Decorator ____________________________________")
"""
@property decorator = Allows you to access a method like an attribute
                    used to define a method as a property (it can be accessed like an attribute)
                Getter method
                Read-only attribute
                Ex. book.title instead of book.get_title()

Benefit: Add additional logic when read, write, or delete attributes
Gives you getter, setter, and deleter method
"""
class Rectangle:

    def __init__(self,rec_id, width, height):
        self._rec_id = rec_id # private attribute "_"
        self._width = width     # private attribute
        self._height = height   # private attribute 

    #Getter method
    @property
    def get_rec_id(self):
        return self._rec_id
    
    @property
    def get_width(self):
        return self._width
    
    @property
    def get_height(self):
        return self._height
    
    #Setter method
    @get_width.setter
    def set_width(self, new_width):
        self._width = new_width

    @get_height.setter
    def set_height(self, new_height):
        self._height = new_height

    
    def display_info(self):
        return f"Id: {self._rec_id}, width: {self._width}cm, height: {self._height}" # using the private attribute
    
    
    def calc_area(self):
        return f"Area: {self._width * self._height}cm²"

    def calc_perimeter(self):
        return f"Perimeter: {2 * (self._width + self._height)}cm"
    

rectangle = Rectangle(1, 10, 5)
print(rectangle.display_info())
print(rectangle.calc_area())
print(rectangle.calc_perimeter())
print(rectangle.get_rec_id)
print(rectangle.get_width)
print(rectangle.get_height)
rectangle.set_width = 15
rectangle.set_height = 8
print(rectangle.display_info())
print(rectangle.calc_area())
print(rectangle.calc_perimeter())
print("_______________________")
r2 = Rectangle(2, 20, 10)
print(r2.display_info())
print(r2.calc_area())
print(r2.calc_perimeter())
print(r2.get_width)
print(r2.get_height)
r2.set_width = 25
r2.set_height = 15
print(r2.display_info())
print(r2.calc_area())
print(r2.calc_perimeter())

print()
print("______________________________ Decorator ____________________________________")
"""
# Decorator = A function that extends the behavior of another function without modifying it
        - Allows you to add functionality to an existing function
        w/o modifying the base function
        Pass the base function as an argument to the decorator

"""
def add_sprinkles(func):
    def wrapper(*args, ** kwargs):
        print("**You add sprinkles**")
        func(*args, ** kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, ** kwargs):
        print("**You add fudge**")
        func(*args, ** kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_ice_cream("Vanilla")
get_ice_cream("Chocolate")
get_ice_cream("Strawberry")

print()
print("-------------------------------------------------------------------------------------------")