n = int(input("Enter Number: "))

a = 0
b = 1
print(a,b,end= " ")
while n > 1:
    c = a + b
    a = b
    b = c
    print(c, end = " ")
    n = n-1
