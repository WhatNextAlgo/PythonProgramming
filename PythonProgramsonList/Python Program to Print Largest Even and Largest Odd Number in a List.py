n =  int(input("Enter number of elments: "))

a = []
for x in range(1,n+1):
    a.append(int(input(f"Enter element {x}: ")))

a.sort()
e = []
o = []
for x in a:
    if x % 2==0:
        e.append(x)
    else:
        o.append(x)

if len(e) > 0:
    print("Largest even number: ",e[-1])

if len(o) > 0:
    print("Largest even number: ",o[-1])
