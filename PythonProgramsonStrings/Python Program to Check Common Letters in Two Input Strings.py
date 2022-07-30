s1= input("Enter first string:")
s2= input("Enter second string:")

a = list(set(s1)&set(s2))
print("The common letters are:")
for x in a:
    print(x, end = " ")