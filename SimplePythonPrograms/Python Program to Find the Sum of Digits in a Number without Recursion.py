n = int(input("Enter Number : "))
acc = 0
while n > 0:
    dig = n % 10
    acc = acc + dig
    n = n// 10

print(acc)