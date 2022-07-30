n = int(input("Enter Number: "))

def is_power_of_two(n):

    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0


def is_power_of_three(n):
    
    if n <= 0:
        return False
    else:
        return n & (n - 1) == (n - 1)


if is_power_of_two(n):
    print(f'{n} is a power of two.')
else:
    print(f'{n} is not a power of two.')


if is_power_of_three(n):
    print(f'{n} is a power of three.')
else:
    print(f'{n} is not a power of three.')




1001
1000

