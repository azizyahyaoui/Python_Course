class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_name(self):
        print(f"Name: {self.name}")

    def walk(self):
        print(f"{self.name} walks around")

    def eat(self):
        print(f"{self.name} eats food")
    
    def sleep(self):
        print(f"{self.name} sleeps")
    
