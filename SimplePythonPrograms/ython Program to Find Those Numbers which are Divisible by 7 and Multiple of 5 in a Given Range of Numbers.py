lower = int(input("Enter a lower limit : "))
upper = int(input("Enter a upper limit : "))

for x in range(lower, upper + 1):
    if (x % 7 == 0) & (x % 5 == 0):
        print(x, end = " ")