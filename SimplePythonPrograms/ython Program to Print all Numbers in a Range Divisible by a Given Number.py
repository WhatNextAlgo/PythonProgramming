lower = int(input("Enter a lower limit : "))
upper = int(input("Enter a upper limit : "))

n  =  int(input("Enter the Number to be divided by : "))

for x in range(lower, upper + 1):
    if x % n == 0:
        print(x, end = " ")