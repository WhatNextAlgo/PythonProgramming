print("""
Area of Circle :  πr2
Perimeter of Circle: 2πr
""")
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return math.pi * 2 * self.radius 

r = float(input("Enter Radius of a Circle: "))
obj = Circle(r)

print("Area of Circle: ",round(obj.area(),2))
print("Perimeter of Circle: ",round(obj.perimeter(),2))