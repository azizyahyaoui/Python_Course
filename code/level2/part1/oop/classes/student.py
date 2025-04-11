class Student:
    class_year = "2021" # class variable
    number_of_students = 0 # class variable
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        Student.number_of_students += 1

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Major: {self.major}, Class Year: {Student.class_year}")
    
    