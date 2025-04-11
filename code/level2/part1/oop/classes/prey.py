from classes.animal import Animal

class Prey(Animal):

  def flee(self):
    print(f"{self.name} flees from predator")