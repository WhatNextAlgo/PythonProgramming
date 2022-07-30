import math
print("""
Area of Triangle Using Heron's Formula:
Consider the triangle ABC with side lengths a, b, and c. To find the area of the triangle we use Heron's formula:

Area = math.sqrt(s(s-a)(s-b)(s-c))
Note that (a + b + c) is the perimeter of the triangle. Therefore, 's' is the semi-perimeter which is: (a + b + c)/2
""")
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))


s = (a + b + c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of a triangle : ",round(area,2))