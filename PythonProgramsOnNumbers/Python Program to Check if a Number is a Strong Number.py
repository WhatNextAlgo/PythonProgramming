

def fact(n):
    if n < 1:
        return 1
    return n * fact(n-1)

def get_digit(n):
    if n == 0:
        return 0
    dig = n % 10
    return fact(dig) + get_digit(n // 10) 
    

n = int(input("Enter Number: "))


if n == get_digit(n):
    print(f"{n} is a strong number.")
else:
    print(f"{n} isn't a strong number.")

