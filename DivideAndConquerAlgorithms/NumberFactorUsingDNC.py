def numerfactor(n):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numerfactor(n-1)
        subP2 = numerfactor(n-3)
        subP3 = numerfactor(n-4)
        return subP1 + subP2 + subP3


print(numerfactor(5))