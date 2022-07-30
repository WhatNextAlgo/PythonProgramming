#Use the Formula: e = 1 + 1/1! + 1/2! + …… 1/n!



nums = int(input("Enter Number: "))
e = 1

def factorial(n):
    if n <=1:
        return 1
    return n * factorial(n-1)

for x in range(1,nums +1 ):
    e = e + (1/factorial(x))

print("The sum of series is",round(e,2))
