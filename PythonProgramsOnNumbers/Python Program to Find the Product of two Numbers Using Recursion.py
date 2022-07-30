x = int(input("Enter Number: "))
y = int(input("Enter Number: "))

def product(a,b):
    if (a<b):
        return product(b,a)
    elif (b!=0):
        return a + product(a,b-1)
    else:
        return 0

print("Product is: ",product(x,y))

