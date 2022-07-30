d = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary")
print(d)
key= input("Enter the key to delete(a-d):")

if key in d:
    del d[key]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)