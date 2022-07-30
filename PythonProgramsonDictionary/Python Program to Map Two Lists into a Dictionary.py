key = []
values = []
n = int(input("Enter number of element in dict: "))

for x  in range(n):
    element = int(input("Enter element" + str(x + 1) + ": "))
    key.append(element)

for x  in range(n):
    element = int(input("Enter element" + str(x + 1) + ": "))
    values.append(element)


d = dict(zip(key,values))
print("The dictionary is:")
print(d)
