def numberfactor(n):
    tb = [1,1,1,2]
    for x  in range(4,n + 1):
        tb.append(tb[x-1] + tb[x-3] + tb[x-4])

    return tb[n]


print(numberfactor(5))