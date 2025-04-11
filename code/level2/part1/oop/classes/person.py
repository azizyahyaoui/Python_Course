class Person:

  def __init__(self, name, age, occupation):
    self.name = name
    self.age = age
    self.occupation = occupation
  
  def display_info(self):
    print(f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}")
