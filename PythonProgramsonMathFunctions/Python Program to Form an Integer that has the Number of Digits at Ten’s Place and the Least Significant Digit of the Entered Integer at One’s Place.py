n  = int(input("Enter Number: "))
temp = n
k = 0

while n > 0:
    k = k +1 
    n = n//10

b = str(temp)
c = str(k)
d = c + b[k-1]
print("The new number formed:",int(d))