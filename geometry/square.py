class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
        square_area = self.side*self.side
        return square_area
    
    def perimeter(self):
        return self.side * 4
    