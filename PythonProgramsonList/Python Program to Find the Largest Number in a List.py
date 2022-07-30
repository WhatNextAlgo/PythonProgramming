n =  int(input("Enter number of elments: "))

a = []
for x in range(1,n+1):
    a.append(int(input(f"Enter element {x}: ")))


a.sort()
print("Largest Element is : ",a[n-1])
