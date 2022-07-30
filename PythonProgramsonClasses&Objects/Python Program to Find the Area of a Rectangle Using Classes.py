class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area_of_rectangle(self):
        return self.l * self.b

l = int(input("Enter lenght of Rectangle: "))
b  = int(input("Enter breadth of Rectangle: "))

obj = Rectangle(l,b)
print("Area of rectangle:",obj.area_of_rectangle())