n = int(input("Enter Number : "))

sum = 0
while n > 0:
    dig = n % 10
    sum = sum + dig
    n = n // 10

print("The total sum of digits is:",sum)