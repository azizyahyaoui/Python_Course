from classes.abstract_classes.c_shape import C_Shape

class C_Triangle(C_Shape):

  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return 0.5 * self.base * self.height

  def print_area(self):
    print(f"The triangle Area: {self.area()}cm²")