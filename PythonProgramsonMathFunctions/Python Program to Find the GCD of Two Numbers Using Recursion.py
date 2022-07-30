a = int(input("Enter first Number: "))
b = int(input("Enter Second Number: "))

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

print("GCD is :",gcd(a,b))