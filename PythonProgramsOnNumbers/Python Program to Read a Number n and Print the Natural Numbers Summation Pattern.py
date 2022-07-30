

n = int(input("Enter Number: "))

for x in range(1,n + 1):
    sum = 0
    p = []
    for y in range(1,x + 1):
        p.append(str(y))
        sum =  sum + y
    patterns = ' + '.join(p)
    print(f"{patterns} = {sum}")