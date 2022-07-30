n = int(input("Enter Number: "))



def print_range(n):
    if n > 0:
        print_range(n -1)
        print(n , end = " ")

print_range(n)