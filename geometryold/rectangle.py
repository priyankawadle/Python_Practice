class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)
    
    def circumfrence(self):
        return 2*(self.length + self.breadth)