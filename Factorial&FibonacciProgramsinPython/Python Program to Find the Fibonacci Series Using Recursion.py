n = int(input("Enter Number : "))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for x in range(n):
    print(fibonacci(x), end = ' ')

