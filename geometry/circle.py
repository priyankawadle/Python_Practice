import math
class Circle:
    def __init__(self,redius):
        self.redius = redius

    def area(self):
        res= ((self.redius**2)*math.pi)
        return res
    
    def circumfrence(self):
        return (self.redius*2*math.pi)
    

        