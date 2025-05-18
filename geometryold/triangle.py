class Triangle:
    def __init__(self,side1,side2,side3,base,height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.height = height

    @property
    def area(self):
        triangle_area = (1/2) * self.base * self.height
        return triangle_area
    @property
    def perimeter(self):
        return self.side1+self.side2+self.side3
    