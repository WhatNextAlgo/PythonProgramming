n = int(input("Enter Number : "))

l = []
while n > 0:
    dig =  n % 2
    l.append(dig)
    n = n // 2

l.reverse()
for x in l:
    print(x,end = " ")
