def counting_sort(alist,largest):
    c = [0] * (largest + 1)

    for x in range(len(alist)):
        c[alist[x]] = c[alist[x]] + 1

    print(c)
    c[0] = c[0] - 1
    
    for x in range(1, largest + 1):
        print(c[x],c[x-1])
        c[x] = c[x] + c[x-1]

    print(c)

    result = [None] * len(alist)

    for x in reversed(alist):
        #print(c[x]," -- ",x)
        result[c[x]] = x
        c[x] = c[x] -1
        print(c)

    return result


        


alist = input('Enter the list of (nonnegative) numbers: ').split()
alist = [int(x) for x in alist]
k = max(alist)
sorted_list = counting_sort(alist, k)
print('Sorted list: ', end='')
print(sorted_list)
