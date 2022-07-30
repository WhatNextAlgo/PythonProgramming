a=[['A',34],['B',21],['C',26]]

for x in range(0, len(a)):
    for y in range(0,len(a)-x-1):
        if a[y][1] > a[y + 1][1]:
            temp = a[y]
            a[y] = a[y + 1]
            a[y + 1] = temp

print(a)