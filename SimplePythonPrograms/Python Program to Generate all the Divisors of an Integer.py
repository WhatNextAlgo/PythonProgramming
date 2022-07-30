n = int(input("Enter Number : "))

for x  in range(1, n + 1):
    if n % x == 0:
        print(x, end = " ")