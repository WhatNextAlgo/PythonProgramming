a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b = []
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.append(x)
print("Non-duplicate items:")
print(unique)