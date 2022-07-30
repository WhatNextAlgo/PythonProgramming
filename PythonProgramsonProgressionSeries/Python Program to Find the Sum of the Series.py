#This is a Python Program to find the sum of series: 1 + 1/2 + 1/3 + ….. + 1/N.

n = int(input("Enter Number: "))
sum1 = 0

for x in range(1,n +1):
    sum1 = sum1 + (1/x)

print("The sum of series is",round(sum1,2))
