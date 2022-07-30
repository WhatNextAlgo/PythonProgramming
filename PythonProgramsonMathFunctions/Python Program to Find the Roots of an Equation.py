print("""
Equation: ax^2 + bx + c 
The roots are calculated using the formula, x = (-b ± √ (b² - 4ac) )/2a
Discriminant is, D = b2 - 4ac
        If D > 0, then the equation has two real and distinct roots.
        If D < 0, the equation has two complex roots.
        If D = 0, the equation has only one real root.
Sum of the roots = -b/a
Product of the roots = c/a
""")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b ** 2 - 4*a*c
d1 = d**0.5
if (d< 0):
    print("The roots are imaginary. ")
else:
    r1 = (-b + d1)/2 *a
    r2 = (-b - d1)/2 *a
    print("The first root: ",round(r1,2))
    print("The second root: ",round(r2,2))