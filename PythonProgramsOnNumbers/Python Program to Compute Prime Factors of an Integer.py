n = int(input("Enter Number: "))

def prime_number(n):
    k = 0
    for x in range(2,n//2 + 1):
        if n % x == 0:
            k = k + 1
    
    if k <= 0:
        return True
    else:
        return False

for x in range(2,n + 1):
    if n % x == 0:
        if prime_number(x):
            print(x, end = " ")