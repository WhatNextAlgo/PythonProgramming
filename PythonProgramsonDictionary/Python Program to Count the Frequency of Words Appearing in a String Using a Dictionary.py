s = input("Enter String: ")
lst = s.split(" ")
d = {}
for x in lst:
    if x in d:
        d[x] += 1

    else:
        d[x] = 1

print(d)