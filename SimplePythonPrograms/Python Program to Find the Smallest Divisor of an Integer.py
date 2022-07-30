n = int(input("Enter Number : "))
for x in range(2, n + 1):
    if n % x == 0:
        print(x)
        break 

