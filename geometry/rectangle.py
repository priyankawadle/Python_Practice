class Rectangle:
  
  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth

  @property  
  def area(self):
    return self.length * self.breadth

  @property  
  def perimeter(self):
    return 2*(self.length + self.breadth)

    