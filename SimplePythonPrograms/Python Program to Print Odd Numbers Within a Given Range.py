
lower = int(input("Enter a lower limit range : "))
upper = int(input("Enter a upper limit range : "))

for x in range(lower, upper + 1):
    if x % 2 != 0:
        print(x, end = " ")
