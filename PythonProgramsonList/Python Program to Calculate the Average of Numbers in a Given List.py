n =  int(input("Enter number of elments: "))

a = []
for x in range(1,n+1):
    a.append(int(input(f"Enter element {x}: ")))

avg = sum(a)/n

print("Average of elements in the list",round(avg,2))
