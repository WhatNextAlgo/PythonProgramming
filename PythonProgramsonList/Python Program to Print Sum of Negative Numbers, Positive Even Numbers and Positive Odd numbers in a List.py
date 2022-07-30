n =  int(input("Enter number of elments: "))

a = []
for x in range(1,n+1):
    a.append(int(input(f"Enter element {x}: ")))

e = 0
o = 0
ne = 0

for x  in a:
    if x >= 0:
        if x % 2 == 0:
            e = e +x
        else:
            o = o + x
    else:
        ne = ne + x
print("Sum of all positive even numbers:",e)
print("Sum of all positive odd numbers:",o)
print("Sum of all negative numbers:",ne)
    

