s = input("Enter String: ")

d = {}
for x in s:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

print(d) 

