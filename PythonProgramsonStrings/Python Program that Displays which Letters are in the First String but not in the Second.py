s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

a = list(set(s1)-set(s2))
print(a)
f1 =   list(set(s1))
f2 =   list(set(s2))
a1 = [x for x  in f1 if x not in f2]
print(a1)
