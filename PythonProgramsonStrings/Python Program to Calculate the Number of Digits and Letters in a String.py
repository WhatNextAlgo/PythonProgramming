s = input("Enter String: ")

d= 0
c = 0

for x in s:
    if x.isdigit():
        d = d + 1
    c = c + 1

        


print("The number of digits is:")
print(d)
print("The number of characters is:")
print(c)
