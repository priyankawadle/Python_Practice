import math

class Circle:
  def __init__(self,radius):
    self.radius = radius
  
  @property
  def area(self):
    pi = math.pi
    return pi*(self.radius**2)
  
  @property
  def circumference(self):
    pi = math.pi
    return 2*pi*(self.radius)