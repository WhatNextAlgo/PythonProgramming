def fibnacci(n):

    r = [-1] * (n + 1)
    r[0] = 0
    r[1] = 1

    for x in range(2,n + 1):
        r[x] = r[x-1] + r[x-2]
    
    return r[n-1]

print(fibnacci(1))
