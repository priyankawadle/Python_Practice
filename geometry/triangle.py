class Triangle:

  def __init__(self, base, height, side_a,side_b,side_c):

    self.base=base
    self.height=height
    self.side_a=side_a
    self.side_b=side_b
    self.side_c=side_c

  @property
  def area(self):
    return .5*self.base*self.height

  @property
  def perimeter(self):
    return self.side_a+self.side_b+self.side_c
    