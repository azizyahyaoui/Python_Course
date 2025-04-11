from classes.abstract_classes.c_shape import C_Shape

class C_Circle(C_Shape):

  def __init__(self,radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius * self.radius

  def print_area(self):
    print(f"The circle Area: {self.area()}cm²")