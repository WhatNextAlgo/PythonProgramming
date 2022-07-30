s = input("Enter String: ")

lst = s.split(" ")

d = {}
for x in lst:
    if x[0] not in d:
        d[x[0]] = [x]
    else:
        if x not in  d[x[0]]:
            d[x[0]] += [x]

print(d)
